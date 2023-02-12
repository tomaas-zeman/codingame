c=gets.to_i
n=gets.to_i
s=0.0
n.times{s+=gets.to_i}
puts (s/c).ceil*(n+1)