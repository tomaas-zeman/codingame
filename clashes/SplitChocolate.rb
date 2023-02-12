m, n = gets.split(" ").collect {|x| x.to_i}

max = [m, n].max
min = m + n - max

puts (max - 1) + (max * (min - 1))