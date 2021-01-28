
In distributional semantics, the contexts in which a word is attested are taken to define its meaning. Contextual similarity is thus a correlate of semantic similarity. Different representations of context are possible, the most prominent model to date is the form of a vector. A word vector can be created, for example, by means of a reference list of vocabulary items, where every reference word is associated with a fixed position, e.g., _ship_ with position 1, _ocean_ with 2, _sky_ with 3, etc. Given a corpus (and a selection criterion for collocates, e.g., within the same sentence), every word in the corpus can be described by the frequency that a reference word occurred as a collocate in the corpus. Assume we want to define the meaning of _frak_, with (exactly) the following attestations in our sample corpus (random samples from [wikiquote](https://en.wikiquote.org/wiki/Battlestar_Galactica_(2003))):

*   _It's in the frakking ship!_
*   _Have you lost your frakkin' mind?_
*   _Oh, for frak's sake, let me see if I can make heads or tails of it._
*   _It's a frakking Cylon._
*   _Our job isn't to be careful, it's to shoot Cylons out of the frakking sky!_

With the following list of reference words: <tt>(ship, ocean, lose, find, brain, mind, head, sky, Cylon, ...)</tt>, we obtain the vector <tt>(1,0,1,0,0,1,1,1,2,...)</tt> for the lemma (lexical entry) _frak_. For practical applications, these vectors are projected into lower-dimensional spaces, e.g., by means of statistical (Schütze 1993) or neural methods (Socher et al. 2011). The process of mapping a word to a numerical vector and its result are referred to as "word embedding". Aside from collocation counts, other methods for creating word embeddings do exist, but they are always defined relative to a corpus.

Embeddings have become a dominating paradigm in natural language processing and machine learning, but, if compiled from large corpora, they require long training periods and thus tend to be re-used. However, embedding distributions often use tool-specific binary formats (cf. [Gensim](https://radimrehurek.com/gensim/models/word2vec.html)), and thus a portability problem arises. CSV and related formats (cf. [SENNA embeddings](https://github.com/baojie/senna/tree/master/embeddings)) are a better alternative, but their application to sense and concept embeddings (as provided, for example, by Rothe and Schütze 2017) is problematic if their distribution is detached from the definition of the underlying sense and concept definitions. With frac, Ontolex-lemon provides a vocabulary for the conjoint publication and sharing of embeddings and lexical information at all levels: non-lemmatized words (ontolex:Form), lemmatized words (ontolex:LexicalEntry), phrases (ontolex:MultiWordExpression), lexical senses (ontolex:LexicalSense) and lexical concepts (ontolex:LexicalConcept).

<div class="note">

> We focus on _publishing and sharing_ embeddings, not on their processing by means of Semantic Web formalisms, and thus, embeddings are represented as untyped or string literals with whitespace-separated numbers. If necessary, more elaborate representations, e.g., using rdf:List, may subsequently be generated from these literals.

</div>

Lexicalized embeddings provide their data via <tt>rdf:value</tt>, and should be published together with their metadata, most importantly

*   procedure/method (<tt>dct:description</tt> with free text, e.g., "CBOW", "SKIP-GRAM", "collocation counts")
*   corpus (<tt>dct:source</tt>)
*   dimensionality (<tt>dct:extent</tt>)

<div class="entity">

> ----
> ### embedding (ObjectProperty)
> **URI:** [http://www.w3.org/nl/lemon/frac#embedding](http://www.w3.org/nl/lemon/frac#embedding)
> The property **embedding** is a relation that maps a frac:Observable into a numerical feature space. An embedding is a structure-preserving mapping in the sense that it encodes and preserves contextual features of a particular frac:Observable (or, an aggregation over all its attestations) in a particular corpus.
> **rdfs:range** ontolex:Element
> **rdfs:domain** frac:Embedding
>
> ---
</div>


<div class="entity">

> ---
> ### Embedding (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#Embedding](http://www.w3.org/nl/lemon/frac#Embedding)
> An **Embedding** is a  representation (of a given frac:Observable (see <tt>frac:embedding</tt>) in a numerical feature space. It is defined by the methodology used for creating it (<tt>dct:description</tt>), the URI of the corpus or language resource from which it was created (<tt>dct:source</tt>). The literal value of an Embedding is  provided by <tt>rdf:value</tt>).
> **SubClassOf:** rdf:value exactly 1 xsd:string, dct:source min 1, dct:description min 1
>
> ---
</div>

</div>

<div class="note">
The use of the term "embedding" adopted here follows the terminology in mathematics: For the embedding of an object  _X_  in another object  _Y_, the embedding _f_ :  _X_  →  _Y_  (alternatively _f_ : _X_ ↪ _Y_) is defined as an  injective, structure-preserving map (morphism). (Rephrased from [https://en.wikipedia.org/wiki/Embedding](https://en.wikipedia.org/wiki/Embedding))  For "embedding" in the sense conventionally used in language technology, see the subclass frac:FixedSizeVector.</div>

<div class="note">
FrAC does not define the type of literal provided in the rdf:value of an embedding. The following examples use JSON literals, this is, however, informative, not normative. Alternative encodings based on tool-specific string representations (e.g., whitespace-separated numbers or comma-separated values) are possible. For string literals or untyped literal values, it is recommended to provide a regular expression that defines how to parse it as part of the description of the Embedding. As an example, the following regular expression for parsing embedding values can be used to parse whitespace-separated numbers (example in Perl):

`split(/[^0-9\.,\-]+/, $value)`

This means that doubles should be provided in the conventional format, not using the exponent notation.

Also note that different subclasses of frac:Embedding may have different encoding strategies.
</div>

<div class="entity">

> ---
> ### FixedSizeVector (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#FixedSizeVector](http://www.w3.org/nl/lemon/frac#FixedSizeVector)
> A **FixedSizeVector** is the value of a frac:embedding into a fixed-size numerical feature space. The literal value (<tt>rdf:value</tt>) of a FixedSizeVector is a list of numbers. The dimensionality of the feature space should be encoded by dct:extent.
> **SubClassOf:** Embedding, dct:extent exactly 1
>
> ---
</div>

Word, sense or concept embeddings as conventionally used in language technology are fixed size vectors. The 50-dimensional [GloVe](https://nlp.stanford.edu/projects/glove/) 6B (Wikipedia 2014+Gigaword 5) embedding for _frak_ is given below:

<tt>frak 0.015246 -0.30472 0.68107 -0.59727 -0.95368 -1.0931 0.58783 -0.19128 0.49108 0.61215 -0.14967 0.68197 0.22723 0.38514 -0.54721 -0.71187 0.21832 0.59857 0.1076 -0.23619 -0.86604 -0.91168 0.26087 -0.42067 0.60649 0.80644 -1.0477 0.67461 0.34154 -0.072511 -1.01 0.35331 -0.35636 0.9764 -0.62665 -0.29075 0.50797 -1.3538 0.18744 0.27852 -0.22557 -1.187 -0.11523 -0.078265 0.29849 0.22993 -0.12354 0.2829 1.0697 0.015366</tt>

As a lemma (LexicalEntry) embedding, this can be represented as follows:

<div class="beispiel">

<div>

<pre>
:frak a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "frak"@en;
  frac:embedding [ 
    a frac:FixedSizeVector;
	rdf:value "[ 0.015246 , -0.30472 , 0.68107,  ... ]"^^rdf:JSON;
	dct:source 
      &lt;http://dumps.wikimedia.org/enwiki/20140102/>,
	  &lt;https://catalog.ldc.upenn.edu/LDC2011T07>;
	dct:extent 50^^^xsd:int;
	dct:description "GloVe v.1.1, documented in Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014\. GloVe: Global Vectors for Word Representation, see https://nlp.stanford.edu/projects/glove/; uncased"@en. ].`
	</pre>

</div>

</div>

In this example, the rdf:value of the embedding is represented my a JSON array (abbreviated).

<div class="note">

As with <tt>frac:Frequency</tt>, we recommend defining resource-specific subclasses of <tt>frac:Embedding</tt> in order to reduce redundancy in the data:

<div class="beispiel">

<div>

<pre>
 # resource-specific embedding class
:GloVe6BEmbedding_50d rdfs:subClassOf frac:FixedSizeVector;
  rdfs:subClassOf 
    [ a owl:Restriction;
	  owl:onProperty dct:source;
	  owl:hasValue
		  &lt;http://dumps.wikimedia.org/enwiki/20140102/>,
		  &lt;https://catalog.ldc.upenn.edu/LDC2011T07> ],
	[ a owl:Restriction;
	  owl:onProperty rdf:value;
	  owl:allValuesFrom rdf:JSON ],
	[ a owl:Restriction;
	  owl:onProperty dct:extent;
	  owl:hasValue 50^^xsd:int ],
	[ a owl:Restriction;
	  owl:onProperty dct:description;
	  owl:hasValue "GloVe v.1.1, documented in Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014\. GloVe: Global Vectors for Word Representation, see https://nlp.stanford.edu/projects/glove/; uncased"@en. ].

# embedding assignment
:frak a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "frak"@en;
  frac:embedding [ 
    a :GloVe6BEmbedding_50d;
	rdf:value "[ 0.015246 , -0.30472 , 0.68107 ,  ... ]"^^rdf:JSON.`</pre>

</div>

</div>

</div>

<div class="note">

Examples for non-word embeddings:

*   [AutoExtend](http://www.cis.lmu.de/~sascha/AutoExtend/): (a method to build) synset and lexeme embeddings, data [here](http://www.cis.lmu.de/~sascha/AutoExtend/embeddings.zip)
*   [SenseGram](https://github.com/uhh-lt/sensegram): sense embeddings, data [here](http://ltdata1.informatik.uni-hamburg.de/sensegram/)
*   [Vec2Synset](http://tudarmstadt-lt.github.io/vec2synset/): (a method to build) WordNet synset (= LexicalConcept) embeddings
*   [Character embeddings](https://minimaxir.com/2017/04/char-embeddings/) are probably beyond the scope of OntoLex, unless characters are regarded LexicalEntries. (Which they could, for languages such as Chinese or Sumerian certainly, but also for Western languages -- given the fact that character-level pseudo entries are sometimes used in dictionaries to describe the phonology and orthography of a language. This is the case, for example, for Grimm's [Deutsches Wörterbuch](http://woerterbuchnetz.de/cgi-bin/WBNetz/wbgui_py?sigle=DWB).)

</div>

</section>

<section>

<div class="entity">

> ---
> ### TimeSeries (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#TimeSeries](http://www.w3.org/nl/lemon/frac#TimeSeries)
> A **TimeSeries** is a sequence of observations represented as numerical values, e.g., sensor data. Every point in the sequence is represented by a fixed number of numerical values. The time series is the concatenation of these values. The obligatory attribute <tt>dct:extent</tt> defines the number of observations (dimensionality) for every individual point of time. 
> **SubClassOf:** Embedding, dct:extent exactly 1
>
> ---
</div>

Note: name to be discussed. Maybe "Sequence".
Example to be provided by Manolis and Sander.
...

Note: Other embeddings are usually obtained by aggregation over multiple attestations in a corpus. TimeSeries, however, can also encode a single observation that serves as a prototype.

Other examples of time series:
- a sequence of contextualized word embeddings to represent longer phrases, e.g., in attention-based neural architectures [REF: Bahdanau, D., Cho, K., & Bengio, Y. (2015, January). Neural machine translation by jointly learning to align and translate. In _3rd International Conference on Learning Representations, ICLR 2015_. -- this ] 
- formant analysis as provided in phonetic analysis by Praat [REF: Boersma, Paul; van Heuven, Vincent (2001). ["Speak and unSpeak with Praat"](http://www.fon.hum.uva.nl/paul/papers/speakUnspeakPraat_glot2001.pdf)  (PDF). _Glot International_. **5** (9/10): 341–347.]

<div class="entity">

> ---
> ### BagOfWords (Class)
> **URI:** [http://www.w3.org/nl/lemon/frac#BagOfWords](http://www.w3.org/nl/lemon/frac#TimeSeries)
> For any frac:Observable, a **frac:BagOfWords** represents the collocates it occurs with in a particular corpus. In a weighted bag of words, every collocate is stored together with a frequency, confidence score or association weight. A bag of words must not define a dct:extent.
>
> **SubClassOf:** Embedding, dct:extent exactly 0
>
> ---
</div>
Bags of words can be compared to word embeddings (in languagte technology) in the sense that they represent infinite-dimensional, uncompressed frequency counts obtained from the aggregation over attestations in a corpus. The interpretability of their respective numerical dimensions, however, depends on the lexical provided along with it, so the normal data structure of a bag of words is not a vector, but a map (from collocates to weights, frequencies or association scores) or a set (of collocates, assuming each collocate is equally weighted). The encoding of the rdf:value must be specified in the dct:description. The example below uses an rdf:JSON literal representing a map. 

Example taken from [Wortschatz](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=frac#coocs), collocations of _frac_ (significant collocates in the same sentence), with frequency scores provided, filtered for significance (log-likelihood):

[sand](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=sand) (508), [mining](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=mining) (82), [Chesterland-based](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Chesterland-based) (75), [wells](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=wells) (73), [DNR](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=DNR) (73), [Silica](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Silica) (53), [fluid](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fluid) (52), [category](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=category) (51), [spill](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=spill) (49), [rigs](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=rigs) (48), [New Canaan](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=New+Canaan) (48), [oil](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=oil) (47), [drilling](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=drilling) (46), [County](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=County) (45), [shale](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=shale) (45), [mine](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=mine) (43), [Permian](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Permian) (41), [tons](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=tons) (40), [Canaan](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Canaan) (39), [gas](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=gas) (39), [More](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=More) (38), [fracturing](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fracturing) (38), [Texas](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Texas) (37), [Monroe](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Monroe) (35), [hydraulic](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=hydraulic) (35), [per](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=per) (35), [judge’s](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=judge%E2%80%99s) (35), [plant](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=plant) (34), [miner](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=miner) (34), [fluids](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fluids) (34), [Alpine](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Alpine) (33), [company](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=company) (33), [crews](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=crews) (30), [producer](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=producer) (28), [used](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=used) (26), [disposal](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=disposal) (25), [million](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=million) (24), [chemicals](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=chemicals) (23), [premium](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=premium) (22), [approximately](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=approximately) (22), [raw](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=raw) (21), [coal](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=coal) (20), [stages](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=stages) (20), [review](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=review) (20), [permit](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=permit) (18), [water](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=water) (18), [industry](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=industry) (18), [industrial](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=industrial) (17), [fees](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=fees) (16), [production](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=production) (16), [attorney](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=attorney) (15), [lines](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=lines) (14), [active](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=active) (13), [Canadian](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=Canadian) (12), [feet](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=feet) (12), [demand](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=demand) (12), [county](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=county) (11), [River](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=River) (11), [major](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=major) (11), [in](https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=in) (11)

<div class="beispiel">

<div>

<pre>
:frac a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "frac"@en;
  frac:embedding [ 
    a :BagOfWords;
    dct:description "Cooccurrences of a word are those words that occur 
    noticeably often together with it. This may be the case as immediate 
    left neighbour, as immediate right neighbour, or in the same sentence. 
    The relevance of a cooccurrence is measured using a significance 
    measure; cooccurrences are ordered by their significance. At the 
    _Leipzig Corpora Collection_ the log-likelihood ratio is used as significance 
    measure and word pairs of little significance are removed.";
    dct:source &lt;https://corpora.uni-leipzig.de/en/res?corpusId=eng_newscrawl-public_2018&word=frac>;
	rdf:value " { \"sand\" : \"508\" , \"mining\" : \"82\" , ... }"^^rdf:JSON.`</pre>

</div>

</div>

</div>

