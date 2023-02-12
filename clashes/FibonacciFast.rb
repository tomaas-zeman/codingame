n = gets.to_i
if n == 1
    puts 0
else
    sequence = [0, 1]
    (n-2).times do
        sequence << sequence[-1] + sequence[-2]
    end
    puts(sequence.join(" "))
end