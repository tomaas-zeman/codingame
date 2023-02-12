n = gets.to_i
inputs = gets.split(" ")
nums = []
for i in 0..(n-1)
    nums << inputs[i].to_i
end
puts "%g" % ("%.2f" % (nums.sum.to_f / n) )