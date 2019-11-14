For plain word embeddings, this is clearly overkill, but it makes sense for embeddings of elements better identified by a URI, e.g., a sense or lemma (lexical entry).

cf.
    AutoExtend: (a method to build) synset and lexeme embeddings
		http://www.cis.lmu.de/~sascha/AutoExtend/
		http://www.cis.lmu.de/~sascha/AutoExtend/embeddings.zip
    SenseGram: sense embeddings, data here
		https://github.com/uhh-lt/sensegram
		http://ltdata1.informatik.uni-hamburg.de/sensegram/
    Vec2Synset: (a method to build) WordNet synset (= LexicalConcept) embeddings
    Character embeddings are probably beyond the scope of OntoLex, unless characters are regarded LexicalEntries. (Which they could, for languages such as Chinese or Sumerian certainly, but also for Western languages -- given the fact that character-level pseudo entries are sometimes used in dictionaries to describe the phonology and orthography of a language. This is the case, for example, for Grimm's Deutsches Wörterbuch [http://woerterbuchnetz.de/cgi-bin/WBNetz/wbgui_py?sigle=DWB].)
		https://minimaxir.com/2017/04/char-embeddings/