# Modelling corpus queries


## Requirements

In the FrAC meeting at Jan 20, 11:00-12:00 CET, we had a long discussion on a richer modelling of collocations:

- represent morphosyntactically defined "slots" between lexical expressions, e.g., "VERB + analyze"
  - we could (ab)use synsem:SyntacticFrame, but then, with observables as "syntactic" arguments
    (but this is a bit of a stretch as collocations aren't necessarily syntactically structured)
- express an ordered collocation with gaps (e.g., ["VERB", "to", "analyse"] should match both ["difficult", "to", "analyse"] and ["difficult", "to", "properly", "analyse"]
  - maybe interpret an ordered collocation just as something that can always have additional elements inserted?
  - we could create wildcard observables that can be inserted, then -- but this is something that needs to mapped to corpus query languages
- represent responses (and calls to) SketchEngine (etc.)
  - shall we just record query strings
- keep it simple
  - we will not invent an RDF-based corpus query language
- keep it generic
  - we will not create dependencies from any particular query language

### Objectives

- 2022-09-29
  1. model colligations (~ collocations with structural/grammatical constraints)
  2. model "keywords in context" as (dynamically generated) attestations from any given corpus
  3. stay away from query semantics

## Proposal

- create query objects (`Query`)
  - `rdf:value`: query (in any corpus query language)
  - `frac:queryLanguage` object property identifying the query language
  - `frac:variables`: JSON array with string values (variable names)
  - `frac:result`: *one* object property pointing to a container of cooccurrences, with element (Seq) order corresponding to variable order in `frac:variables`
  - `frac:Cooccurrence` as superclass of collocation, carries attestations (links to corpus matches = keyword in context). In the context of corpus queries, a cooccurrence represents one or multiple query terms that can be observed in a corpus. A query term is a partial description of (aspects of) elements that can be observed in a corpus. This could be, for example,  a string value (~ `ontolex:Form`), a token with a particular lemma (~ `ontolex:LexicalEntry`), a particular sense of that lexical entry (~ `ontolex:LexicalSense`), the annotation of a lexicalization-independent concept (~ `ontolex:LexicalConcept`), or any custom collection of constraints of a word (~ `morph:GrammaticalMeaning`) or phrase (~ `decomp:Constituent`). In the query languages CQP or  Tiger, this would correspond to a set of annotations grouped together with angular brackets (e.g., `[tok="play", pos=/V.*/]` for verbal uses of _play_).
- depending on the corpus query language used, there is a mapping from positions in a collocation to positions in a query

Note: The classical keyword-in-context (KWIC) view can be modelled as follows:
- one attestation corresponds to exactly one single line (result)
- the KWIC string is the `rdf:value` of the attestation. Optionally, metadata about highlighting could be added (in the string, but not in machine-readable form)
- one cooccurrence object provides multiple resilts (lines=contexts for keywords), but these have no order (they may have a serialization order in a format, but not explicitly encoded)
- vocabulary needs to feature a fully worked-out example for replicating KWIC view.

### issues

- 2022-09-29: "frac:corpus" seems to sound misleading. "dct:source"? NB: wasn't there a `frac:locus` property *in addition to* frac:corpus ???

### changes/updates

- 29-09-2022: QueryResult class renamed to Query, the original name seems to have been misunderstood as compound "query result" although it was meant to mean "query/result" (i.e., "or"). An alternative name could be the more neutral "SyntacticPattern", but then, the "result" property should be renamed ("response"?). The original name was "query/response", but this was felt to be too procedural.
- 29-09-2022: clarification: query language property should be an object property
- 29-09-2022: revision: `frac:variables` should not point to a literal (originally: json array), but to an RDF Seq (list?) of literals
- 29-09-2022: clarification: there is one `result` property for any query (in a particular corpus)
- 29-09-2022: description of cooccurrence *in this context*
- 29-09-2022: note on keywords in context (KWIC)

### history

- 29-09-2022: sample modelled [MI], discussion at OntoLex-FrAC; revision/clarification [CC]
- 02-03-2022: initial discussion at OntoLex-FrAC
  - cooccurrence as superclass of collocation
- 01-20-2022: initial proposal 
  - create query/response objects
    - attribute query (in any corpus query language) => `rdf:value`
    - attribute query language
    - attribute variables: json array with string values (variable names)
    - response: set of ordered collocations, with element order corresponding to variables
      [ attestations can be indirectly linked via collocations ]
  - depending on the corpus query language used, there is a mapping from positions in a collocation to positions in a query
  - shall we rename collocation to Cooccurrence
  - diagram uses `Observation` as superclass already

## practical application
- modelling complex syntactic patterns for collocation analysis, etc.
- client creates a query/response object without responses
- server returns a query/response object with responses

## diagram

Note that we use a number of minor modifications to the official diagram. In particular, we use the `Observation` class as a generalization over FrAC classes in order to produce a simpler diagram. Adjustments from 2022-09-29 have not been worked in, yet.

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-query.puml?cache=no)

## contributors

- CC - Christian Chiarcos
- MI - Max Ionov
