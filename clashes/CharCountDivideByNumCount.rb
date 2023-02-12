text = gets.chomp

def count(regex, text)
  text.split(//).inject(0) {|count, char| char =~ regex ? count + 1 : count}
end

num_count = count(/\d/, text)
char_count = count(/[[:alpha:]]/, text)

puts char_count / num_count