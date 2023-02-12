STDOUT.sync = true

# w: width of the building.
# h: height of the building.
w, h = gets.split(' ').map { |x| x.to_i }
n = gets.to_i # maximum number of turns before game over.
x, y = gets.split(' ').map { |x| x.to_i }

movements = {
    :U => {:x => 0, :y => -1, :opposite => :D},
    :D => {:x => 0, :y => 1, :opposite => :U},
    :L => {:x => -1, :y => 0, :opposite => :R},
    :R => {:x => 1, :y => 0, :opposite => :L}
}

borders = {
    :U => 0, :D => h, :L => 0, :R => w
}

loop do
  bomb_dir = gets.chomp # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

  bomb_dir.split(//).each do |direction_string|
    direction = direction_string.to_sym

    change_x = ((x - borders[direction]).abs.to_f / 2).ceil * movements[direction][:x]
    change_y = ((y - borders[direction]).abs.to_f / 2).ceil * movements[direction][:y]

    borders[movements[direction][:opposite]] = [:L, :R].include?(direction) ? x : y

    x += change_x
    y += change_y
  end

  puts "#{x} #{y}"
end