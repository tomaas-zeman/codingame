command = gets.chomp

text = command.match(/write ([^\.]*)\./)
text = text.nil? ? "Syntax Error" : text.captures.first

repeat = command.match(/(\d+) times/)
repeat = repeat.nil? ? 1 : repeat.captures.first.to_i

repeat.times{puts text}