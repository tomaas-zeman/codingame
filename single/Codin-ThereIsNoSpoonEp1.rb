STDOUT.sync = true # DO NOT REMOVE
# Don't let the machines win. You are humanity's last hope...

width = gets.to_i # the number of cells on the X axis
height = gets.to_i # the number of cells on the Y axis

rows = []
height.times do
    line = gets.chomp # width characters, each either 0 or .
    rows << line.split(//)
end

cols = []
width.times {|col| cols << rows.map {|row| row[col]}}

width.times do |col|
    height.times do |row|
        if rows[row][col] != "0" or cols[col][row] != "0"
            next
        end
        
        x = Array.new(rows[row][col+1..-1]).index("0")
        y = Array.new(cols[col][row+1..-1]).index("0")
        
        right = x.nil? ? "-1 -1" : "#{x + col + 1} #{row}"
        bottom = y.nil? ? "-1 -1" : "#{col} #{y + row + 1}"
        puts "#{col} #{row} #{right} #{bottom}"        
    end
end