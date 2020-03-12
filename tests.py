from packages.p_board_functions 	import f_generate_seed, f_create_empty_board, f_print_progression, f_seed_to_string, f_string_to_seed, f_is_it_a_seed, f_is_it_an_integer
from packages.p_decisional 			import f_genererate_box
from packages.p_dic_functions 		import f_dic_biomes_creation, f_max_height_of_trees
from packages.p_image_creation 		import f_create_image_header, f_create_image_body
from packages.p_trees_generation 	import f_generate_trees



v_dic_biomes = f_dic_biomes_creation()

print(f_max_height_of_trees(v_dic_biomes))
