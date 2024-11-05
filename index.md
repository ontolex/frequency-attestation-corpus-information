---
title: The Ontolex Module for Frequency, Attestation and Corpus Information
author:
- name: Christian Chiarcos
  companyURL: https://www.uni-augsburg.de/de/fakultaet/philhist/professuren/angewandte-computerlinguistik/
  company: Applied Computational Linguistics, University of Augsburg, Germany
- name: John P. McCrae
  companyURL: https://www.universityofgalway.ie/
  company: University of Galway
- name: Besim Kabashi
  companyURL: https://www.linguistik.phil.fau.de/
  company: Corpus and Computational Linguistics, Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany
- name: Fahad Khan
  companyURL: www.ilc.cnr.it/
  company: Istituto di Linguistica Computazionale <<A. Zampolli>>, Italy
- name: Ciprian-Octavian Truică
- name: Katerina Gkirtzou
- name: Sander Stolk
- name: Thierry Declerck
- name: Jesse de Does
- name: Katrien Depuydt
- name: Elena-Simona Apostol
- name: Max Ionov
  companyURL: https://www.uni-koeln.de/
  company: Institute for Digital Humanities, University of Cologne, Germany
date: 2024-11-05
---

<section id="abstract">

## Abstract

This document describes the _module for frequency, attestation and corpus information_ of the OntoLex Lexicon Model for Ontologies (_OntoLex-Lemon_) developed by the W3C Community Group Ontology-Lexica. The module is targeted at complementing dictionaries and other linguistic resources containing lexicographic data with a vocabulary to express

*   corpus-derived information (frequency and cooccurrence information, collocation analysis, distributional similarity),
*   pointers from lexical resources to corpora and other collections of text (attestations, examples),
*   the linking of corpora and linguistic primary data with lexical information (dictionary linking), and
*   distributional semantics (collocation vectors, word embeddings, sense embeddings, concept embeddings).

The module tackles use cases in corpus-based lexicography, corpus linguistics and natural language processing, and operates in combination with the _OntoLex-Lemon_ core module (_Lemon_), as well as with other _lemon_ modules.
</section>

<section id="sotd">

## Status of this Document

 This specification was published by the Ontology-Lexicon Community Group. It is not a W3C Standard nor is it on the W3C Standards Track. Please note that under the W3C Community Final Specification Agreement (FSA) other conditions apply. Learn more about W3C Community and Business Groups.

This specification was published by the OntoLex Community Group. It is not a W3C Standard nor is it on the W3C Standards Track. Please note that under the W3C Community Contributor License Agreement (CLA) there is a limited opt-out and other conditions apply. Learn more about W3C Community and Business Groups.

This document is an official report of the OntoLex community group. It does not represent the view of single individuals but reflects the consensus and agreement reach as part of the regular group discussions. The report should be regarded as the official specification of lemon.

If you wish to make comments regarding this document, please send them to public-ontolex@w3.org (subscribe, archives).

</section>

<section id="introduction">

## Introduction


[OntoLex-Lemon](https://www.w3.org/2016/05/ontolex/) provides a [core](https://www.w3.org/2016/05/ontolex/#core) vocabulary to represent _linguistic information_ associated to ontology and vocabulary elements. The model follows the principle of _semantics by reference_ in the sense that the semantics of a [lexical entry](https://www.w3.org/2016/05/ontolex/#LexicalEntry) is expressed by reference to an individual, class or property defined in an ontology. The OntoLex module for Frequency, Attestations and Corpus-Based Information (OntoLex-FrAC) complements OntoLex-Lemon with the capability of including information drawn from or found in corpora and linguistic primary data.

In particular, the model's primary motivation is to provide a means to link lexical resources to corpora and other collections of text, and to express the relationship between lexical information and the primary data from which it is derived. As such this module will:

1.  Extend the use of OntoLex-Lemon to support digital lexicography,
2.  Improve application and applicability of OntoLex-Lemon in natural language processing,
3.  Contribute to the integration of lexicography, AI and human language technology communities,
4.  Provide a method of representing this information in a way that is compatible with the existing OntoLex-Lemon model.

<section id="namespaces">

### Namespaces

This is a list of relevant namespaces that will be used in the rest of this document:

OntoLex module for frequency, attestation and corpus information

```
@prefix frac: <http://www.w3.org/ns/lemon/frac#> .
```

OntoLex (core) model and other _lemon_ modules:

```
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix synsem: <http://www.w3.org/ns/lemon/synsem#> .
@prefix decomp: <http://www.w3.org/ns/lemon/decomp#> .
@prefix vartrans: <http://www.w3.org/ns/lemon/vartrans#> .
@prefix lime: <http://www.w3.org/ns/lemon/lime#> .
@prefix lexicog: <http://www.w3.org/ns/lemon/lexicog#> .
```

Other models [TO REVIEW]:

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix skos: <http://www.w3.org/2004/02/skos#>.
@prefix dbr: <http://dbpedia.org/resource/>.
@prefix dbo: <http://dbpedia.org/ontology/>.
@prefix void: <http://rdfs.org/ns/void#>.
@prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#>.
@prefix dct: <http://purl.org/dc/terms/>.
@prefix provo: <http://www.w3.org/ns/prov#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
@prefix oa: <http://www.w3.org/ns/oa#>.
@prefix aat: <http://vocab.getty.edu/aat/>.
@prefix voaf: <http://purl.org/vocommons/voaf#>.
@prefix dcam: <http://purl.org/dc/dcam/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dcmitype: <http://purl.org/dc/dcmitype/> 

```
</section>

<section id="overview">

### Overview of the Module

The following diagram depicts the OntoLex module for frequency, attestation and corpus information (_OntoLex-FrAC_). Boxes represent classes of the model. Arrows with filled heads represent object properties. Arrows with empty heads represent `rdfs:subClassOf`. Vocabulary elements introduced by this module are shaded grey (classes) or set in _italics_.


<figure id="overview-figure">
![](https://raw.githubusercontent.com/acoli-repo/frac-addenda/master/img/diagram-2023.png)
<figcaption>OntoLex Module for Frequency, Attestation and Corpus Information (_FrAC_), overview</figcaption>
</figure>

</section>
</section>

<section id="observations">

## Observations and Observables

OntoLex-FrAC provides the necessary vocabulary to express *observations* obtained from a language resource about any linguistic or conceptual entity that can be observed in a corpus ("observable"). By observable, we mean 

- any *lexical entity* that can be described with OntoLex (including, but not limited to OntoLex core classes `ontolex:LexicalEntry`, `ontolex:Form`, `ontolex:LexicalSense` or `ontolex:LexicalConcept`), as well as
- any *ontological entity* from a knowledge graph (corresponding to the object of an `ontolex:denotes`, `ontolex:reference` or `ontolex:isConceptOf` property). 

The top-level concepts of OntoLex-FrAC are thus `frac:Observable` and `frac:Observation`, complemented by a designating where the observation has been `frac:observedIn`.

<section class="entity">

#### Observable (Class)

**URI:** [http://www.w3.org/nl/lemon/frac#Observable](http://www.w3.org/nl/lemon/frac#Observable)

**Observable** is an abstract superclass for any element of a lexical resource that frequency, attestation or corpus-derived information can be expressed about. This includes, among others, `ontolex:LexicalEntry`, `ontolex:LexicalSense`, `ontolex:Form`, and `ontolex:LexicalConcept`. Elements that FrAC properties apply to  must be observable in a corpus or another linguistic data source.
</div>

</section>

<figure>
![](img/ontolex-element.png "frac:Observable")
<figcaption>`frac:Observable` as a superclass of ontolex:LexicalEntry, ontolex:Form, ontolex:LexicalSense and ontolex:LexicalConcept</figcaption>
</figure>

</section>

