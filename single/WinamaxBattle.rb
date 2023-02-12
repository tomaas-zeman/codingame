def card_value(card_name)
  card_name_parts = card_name.split(//)
  %w(2 3 4 5 6 7 8 9 10 J Q K A).index(card_name_parts[0, card_name_parts.size - 1].join)
end

p1_cards = []
n = gets.to_i # the number of cards for player 1
n.times do
  p1_cards << card_value(gets.chomp) # the n cards of player 1
end

p2_cards = []
m = gets.to_i # the number of cards for player 2
m.times do
  p2_cards << card_value(gets.chomp) # the m cards of player 2
end

STDERR.puts("#{p1_cards.to_s} #{p2_cards.to_s}")

def resolve_war(p1_cards, p2_cards, p1_war_stack=[], p2_war_stack=[])
  if (p1_cards.size < 5 or p2_cards.size < 5)
    return [:pat]
  else
    if p1_cards[4] == p2_cards[4]
      return resolve_war(p1_cards.drop(4), p2_cards.drop(4), (p1_war_stack + p1_cards.take(4)).flatten, (p2_war_stack + p2_cards.take(4)).flatten)
    elsif p1_cards[4] > p2_cards[4]
      p1_cards = (p1_cards.drop(5) + p1_war_stack + p1_cards.take(5) + p2_war_stack + p2_cards.take(5)).flatten
      p2_cards = p2_cards.drop(5)
    else
      p2_cards = (p2_cards.drop(5) + p1_war_stack + p1_cards.take(5) + p2_war_stack + p2_cards.take(5)).flatten
      p1_cards = p1_cards.drop(5)
    end
  end

  return [:ok, p1_cards, p2_cards]
end

rounds = 1
loop do
  if p1_cards.first == p2_cards.first
    status, p1_cards_after_war, p2_cards_after_war = resolve_war(p1_cards, p2_cards)
    case status
    when :pat
      puts 'PAT'
      break
    when :ok
      p1_cards = p1_cards_after_war
      p2_cards = p2_cards_after_war
    end
  else
    p1_card = p1_cards.shift
    p2_card = p2_cards.shift
    p1_cards = p1_cards + [p1_card, p2_card] if p1_card > p2_card
    p2_cards = p2_cards + [p1_card, p2_card] if p1_card < p2_card
  end

  if p1_cards.empty?
    puts "2 #{rounds}"
    break
  end
  if p2_cards.empty?
    puts "1 #{rounds}"
    break
  end

  rounds += 1
end