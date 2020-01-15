require 'gpx'

def run_clean (filename, cleaner, min1, min2, max1, max2)
    gpx_file = GPX::GPXFile.new(:gpx_file => filename)
    area = GPX::Bounds.new(
        min_lat: min1,
        min_lon: min2,
        max_lat: max1,
        max_lon: max2
    )
    gpx_file.crop(area)
    gpx_file.write(cleaner)
    puts "Your file is complete."
end

# Declare start wizard method
def start_wizard
    prompt = "> "
	puts prompt + "Enter map filename (no extension):"
	filename = $stdin.gets.chomp + ".gpx"

	puts prompt + "Enter name for clean map (no extension):"
    cleaner = $stdin.gets.chomp + ".gpx"

    puts prompt + "Enter minimum latitude:"
    minlat = $stdin.gets.chomp

    puts prompt + "Enter minimum longitude:"
    minlon = $stdin.gets.chomp

    puts prompt + "Enter maximum latitude:"
    maxlat = $stdin.gets.chomp

    puts prompt + "Enter maximum longitude:"
	maxlon = $stdin.gets.chomp

    puts "So your filename is #{filename}.
And the clean will be #{cleaner}.
Min lat and long are #{minlat} and #{minlon}.
Max lat and long are #{maxlat} and #{maxlon}.
Is this correct (y or n)?"

	# Confirm the creation of the file
    response = $stdin.gets.chomp

	case response
		when 'Y', 'y', 'yes', 'Yes'
            run_clean filename, cleaner, minlat, minlon, maxlat, maxlon

		else
			puts prompt + "Do you want to start again (y / n)?"
			response = $stdin.gets.chomp

			case response
				when 'Y', 'y', 'yes', 'Yes'
                    start_wizard()

				else
					exit
			end
	end
end

# Start execution
begin
	start_wizard()
end