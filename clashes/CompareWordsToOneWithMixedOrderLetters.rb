n = gets.to_i
scr = gets.chomp.downcase.split(//).sort
n.times do
    acc = gets.chomp
    if acc.downcase.split(//).sort == scr
        puts acc
        break
    end
end