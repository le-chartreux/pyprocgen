# Class diagram of the project
This file is a mermaid.js-style class diagram. To see the diagram, past the following in
[mermaid.js web editor](https://mermaid-js.github.io/mermaid-live-editor/).

	classDiagram
	  class cl_biome{
	    nom_biome : Chaîne
	    temp_min : Réel
	    temp_max : Réel
	    pluv_min : Réel
	    pluv_max : Réel
	    coul : Chaîne

	    m_in_range(self) Booléen
	  }

	  class cl_tree{
	    nom_arbre : String
	    prob_arbre : Réel
	    body : Liste<Liste<Chaîne>>

	    m_get_height(self) Entier
	    m_get_width(self) Entier
	  }



	  class cl_encyclopedie{
	    nom : Chaîne

	    m_get_arbres(self) List<cl_tree>
	    m_get_tree_info(self, nom_arbre) cl_tree
		m_max_height_of_trees(self) integer
	  }


	  cl_biome "0..*" -- "0..*" cl_tree
	  cl_biome "0..*" -- "0..*" cl_encyclopedie
