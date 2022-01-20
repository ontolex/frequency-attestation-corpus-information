# Diagram drafts

originally done with Excel, PlantUml is easier to maintain and edit. The UML diagram is, however, not the recommended visualization, but only used for drafting.

## Current diagram:

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram.puml?cache=no)

## Suggested simplification:

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-observation.puml?cache=no)

Aspects of simplification:
- introduce a common superclass over FrAC elements (`frac:Observation')
  - attributes: `dc:description` and `rdf:value`
  - properties: `corpus` (link with corpus)
    - note: this means that `locus` is merged with `corpus`; maybe different name?
- abandon `ContextualRelation`
