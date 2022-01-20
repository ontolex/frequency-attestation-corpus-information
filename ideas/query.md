# Modelling corpus queries

In the FrAC meeting at Jan 20, 11:00-12:00 CET, we had a long discussion on a richer modelling of collocations.

Requirements:
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

Suggestion:
- create query/response objects
  - attribute query (in any corpus query language) => `rdf:value`
  - attribute query language
  - attribute variables: json array with string values (variable names)
  - response: set of ordered collocations, with element order corresponding to variables
    [ attestations can be indirectly linked via collocations ]
- depending on the corpus query language used, there is a mapping from positions in a collocation to positions in a query

? shall we rename collocation to Cooccurrence

practical application:
- client creates a query/response object without responses
- server returns a query/response object with responses


![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-query.puml?cache=no)
