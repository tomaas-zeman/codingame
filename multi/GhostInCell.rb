require 'set'

STDOUT.sync = true

Factory = Struct.new(:id, :links, :owner, :cyborgs, :production) do
  def initialize(id, links=[], owner=:neutral, cyborgs=0, production=0)
    super(id, links, owner, cyborgs, production)
  end
end
Link = Struct.new(:source_factory_id, :dest_factory_id, :distance)
Army = Struct.new(:owner, :from_factory_id, :to_factory_id, :cyborgs, :turns_to_arrive)
Bomb = Struct.new(:owner, :from_factory_id, :to_factory_id, :turns_to_explode)

def get_owner(value)
  case value
  when 1
    :me
  when -1
    :enemy
  when 0
    :neutral
  else
    raise StandardError, "Unexpected value: #{value}"
  end
end

def pick_random_item(items)
  items[rand(items.size)]
end

def find_close_opposite_factory(factories, initial_factory)
  queue = [initial_factory]
  loop do
    factory = queue.pop

    if factory.owner != initial_factory.owner
      return factory
    end

    next_step = factory.links.map { |l| factories[l.dest_factory_id] }

    # remove duplicates from the new list to prevent loops (not perfect BFS but at least simple)
    queue = (next_step - queue) + queue
  end
end

army_size = 5
bombs_left = 2

factory_count = gets.to_i # the number of factories
factories = factory_count.times.map { |id| Factory.new(id) }

link_count = gets.to_i # the number of links between factories
link_count.times do
  factory_1, factory_2, distance = gets.split(' ').map { |x| x.to_i }
  factories[factory_1].links << Link.new(factory_1, factory_2, distance)
  factories[factory_2].links << Link.new(factory_2, factory_1, distance)
end

loop do
  commands = []

  armies = []
  bombs = []

  entity_count = gets.to_i # the number of entities (e.g. factories and troops)
  entity_count.times do
    id, type, arg1, arg2, arg3, arg4, arg5 = gets.split(' ')
    id = id.to_i
    arg1 = arg1.to_i
    arg2 = arg2.to_i
    arg3 = arg3.to_i
    arg4 = arg4.to_i
    arg5 = arg5.to_i

    case type
    when 'FACTORY'
      factories[id].owner = get_owner(arg1)
      factories[id].cyborgs = arg2
      factories[id].production = arg3
    when 'TROOP'
      armies << Army.new(get_owner(arg1), arg2, arg3, arg4, arg5)
    when 'BOMB'
      bombs << Bomb.new(get_owner(arg1), arg2, arg3, arg4)
    end
  end

  my_factories = factories.select { |f| f.owner == :me }.sort { |f1, f2| f2.cyborgs - f1.cyborgs }
  not_my_factories = factories - my_factories.sort { |f1, f2| f2.production - f1.production}
  enemy_factories = factories.select { |f| f.owner == :enemy_factories }.sort { |f1, f2| f2.cyborgs - f1.cyborgs }
  #enemy_bombs = bombs.select { |b| b.owner == :enemy }

  if my_factories.empty?
    puts 'WAIT'
    next
  end

  if bombs_left > 0 && !enemy_factories.empty?
    factory = find_close_opposite_factory(factories, enemy_factories.first)
    commands << "BOMB #{factory.id} #{enemy_factories.first.id}"
  end

  # TODO: try to send less then a production, if production is low, wait a turn
  my_factories.select { |f| f.cyborgs >= army_size * 2 }.each do |f|
    armies_to_send = (f.cyborgs / army_size) - 1  # leave one army still at home
    [armies_to_send, not_my_factories.size].min.times do |i|
      commands << "MOVE #{f.id} #{not_my_factories[i].id} #{army_size}"
    end
  end

  puts commands.empty? ? "WAIT" : commands.join(" ; ")
end
