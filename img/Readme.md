# Diagram drafts

originally done with PPT, PlantUml is easier to maintain and edit. The UML diagram is, however, not the recommended visualization, but only used for drafting.

## Current official diagram

Until COLING paper is accepted, the following remains official:

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram.puml?cache=no)

## Suggested simplification

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-observation-compact.puml?cache=no)

- May 2022: simplification suggested
- May 2022: equivalent "compact view"
- July 2022:
  - frac:locus restored
  - frac:gloss => frac:attestationGloss

### Simplification discussion

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-observation.puml?cache=no)

Aspects of simplification:
- introduce a common superclass over FrAC elements (`frac:Observation')
  - attributes: `dc:description` and `rdf:value`
  - properties: `corpus` (link with corpus)
    - note: this means that `locus` is merged with `corpus`; maybe different name?
- abandon `ContextualRelation`
- eliminate `quotation`. Instead, use `rdf:value`
- rename `attestationGloss`  to `gloss`: No other glosses here.

> *Note*: In the final diagram, maybe we don't draw arrows between classes and `Observation`, but, instead, put all observations into a box, label it "subclasses of Observation" and put the Observation class with its properties there
> This is the "compact view"


