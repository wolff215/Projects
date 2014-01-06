#!usr.bin.env ruby

File.open('todo.txt', 'r') do |file|
  counter = 1
  file.readlines.each do |line|
    name,created,completed = line.chomp.split(/,/)
    printf("%3d - %s\n",counter,name)
    printf("	  Created   : %s\n",created)
    unless completed.nil?
      printf("	    Completed : %s\n",completed)
    end
    counter += 1
  end
end
