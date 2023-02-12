def round(num)
    return "%g" % ("%.1f" % (num) ) 
 end
 
 x_1, y_1 = gets.split(" ").collect {|x| x.to_f}
 x_2, y_2 = gets.split(" ").collect {|x| x.to_f}
 
 puts "#{round((x_1 + x_2)/2)} #{round((y_1 + y_2)/ 2)}"