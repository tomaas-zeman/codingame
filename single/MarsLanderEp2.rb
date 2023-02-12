STDOUT.sync = true # DO NOT REMOVE

surface_n = gets.to_i # the number of points used to draw the surface of Mars.

land = []
surface_n.times do
  # land_x: X coordinate of a surface point. (0 to 6999)
  # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
  land_x, land_y = gets.split(" ").collect { |x| x.to_i }
  land << {:x => land_x, :y => land_y}
end

flat_area_x = land

# game loop
loop do
  # h_speed: the horizontal speed (in m/s), can be negative.
  # v_speed: the vertical speed (in m/s), can be negative.
  # fuel: the quantity of remaining fuel in liters.
  # rotate: the rotation angle in degrees (-90 to 90).
  # power: the thrust power (0 to 4).
  x, y, h_speed, v_speed, fuel, rotate, power = gets.split(" ").collect { |x| x.to_i }

  # Write an action using puts
  # To debug: STDERR.puts "Debug messages..."


  # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
  puts "-20 3"
end