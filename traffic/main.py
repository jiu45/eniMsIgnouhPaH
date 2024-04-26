import general

gen = general.General()

gen.graph()

gen.shortest_path_all()

gen.take_most_important()

print(gen.shortest_path({'StopId': 417}, {'StopId': 424}))

gen.shortest_path_to_file({'StopId': 417}, {'StopId': 424})