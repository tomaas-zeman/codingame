c = gets.chomp
l = gets.to_i
if l < 3
    puts "CAN'T"
else
    x = (l.to_i - 1) / 2
    puts("#{'*'*x}#{c}#{'*'*x}")
end