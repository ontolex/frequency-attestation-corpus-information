PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX frac: <http://www.w3.org/ns/lemon/frac#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#>
PREFIX lexicog: <http://www.w3.org/ns/lemon/lexicog#>
PREFIX dct: <http://purl.org/dc/terms/> 

SELECT DISTINCT ?collocation ?member ?order
WHERE {
	?collocation a frac:Collocation ;
	?prop ?member .
	FILTER(?prop=rdfs:member || 
		regex(str(?prop),".*#_[0-9]+$"))
	OPTIONAL {
		?collocation ?nrel ?member .
		FILTER(regex(str(?nrel),".*#_[0-9]+$"))
		BIND(replace(str(?nrel),".*#_([0-9]+)$","$1")
		AS ?order )
	}
} ORDER BY ?collocation ?order ?member

-----------------------------------------------------------------------------------------
| collocation                        | member                                   | order |
=========================================================================================
| <http://ickweessoochni.ch/col_1>   | <http://ickweessoochni.ch/point_sense_1> | "1"   |
| <http://ickweessoochni.ch/col_1>   | <http://ickweessoochni.ch/have>          | "2"   |
| <http://ickweessoochni.ch/col_2_1> | <http://ickweessoochni.ch/point_sense_1> | "1"   |
| <http://ickweessoochni.ch/col_2_1> | <http://ickweessoochni.ch/see>           | "2"   |
| <http://ickweessoochni.ch/col_2_2> | <http://ickweessoochni.ch/point_sense_1> | "1"   |
| <http://ickweessoochni.ch/col_2_2> | <http://ickweessoochni.ch/take>          | "2"   |
-----------------------------------------------------------------------------------------


PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX frac: <http://www.w3.org/ns/lemon/frac#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#>
PREFIX lexicog: <http://www.w3.org/ns/lemon/lexicog#>
PREFIX dct: <http://purl.org/dc/terms/> 

SELECT DISTINCT ?collocation ?string
WHERE {
	{ SELECT ?collocation
	  (GROUP_CONCAT(?wrep; separator=" ")
	   AS ?string)
	  WHERE {
	  	{ SELECT ?collocation ?member 
	  			 ?wrep ?order 
	  	  WHERE {
	  	  	?collocation a frac:Collocation ;
	  	  		?prop ?member .
	  	  	FILTER(?prop=rdfs:member || 
	  	  		regex(str(?prop),".*#_[0-9]+$"))
	  	  	?member ((^ontolex:sense)?/ontolex:canonicalForm)?/ontolex:writtenRep ?wrep.
	  	  	OPTIONAL {
	  	  		?collocation ?nrel ?member .
	  	  		FILTER(regex(str(?nrel),".*#_[0-9]+$"))
	  	  		BIND(replace(str(?nrel),".*#_([0-9]+)$","$1")
	  	  		AS ?order)
	  	  	}
	  	  } GROUP BY ?collocation ?member ?wrep ?order
	  	    ORDER BY ?collocation ?order ?member
	  	}
	  } GROUP BY ?collocation
	}
}


-----------------------------------------------------
| collocation                        | string       |
=====================================================
| <http://ickweessoochni.ch/col_2_2> | "point take" |
| <http://ickweessoochni.ch/col_2_1> | "point see"  |
| <http://ickweessoochni.ch/col_1>   | "point have" |
-----------------------------------------------------


As evident from these results (and by comparison with the examples, the OCDS notation `+` does not preserve order).

Note that here, we only generated sequences of canonical forms. By substituting `ontolex:canonicalForm` with `ontolex:lexicalForm`, we can generate all candidate forms