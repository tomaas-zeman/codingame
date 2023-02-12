gets.chomp.split(/ /).each do |word|
    puts word.split(//).map{|c| c.ord}.sum
end