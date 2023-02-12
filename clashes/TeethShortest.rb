gets.to_i.times{gets.chomp.split(//).each{|c|c=='0'?print('-'): print(c)}
puts}