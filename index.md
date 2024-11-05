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

**URI:** [http://www.w3.org/ns/lemon/frac#Observable](http://www.w3.org/ns/lemon/frac#Observable)

**Observable** is an abstract superclass for any element of a lexical resource that frequency, attestation or corpus-derived information can be expressed about. This includes, among others, `ontolex:LexicalEntry`, `ontolex:LexicalSense`, `ontolex:Form`, and `ontolex:LexicalConcept`. Elements that FrAC properties apply to  must be observable in a corpus or another linguistic data source.
</div>

</section>

<figure>

![](img/ontolex-element.png "frac:Observable")

<figcaption>`frac:Observable` as a superclass of ontolex:LexicalEntry, ontolex:Form, ontolex:LexicalSense and ontolex:LexicalConcept</figcaption>

</figure>

For OntoLex, we assume that frequency, attestation and corpus information can be provided about _every_ linguistic content element in the OntoLex-Lemon core model and in existing or forthcoming OntoLex modules. This includes `ontolex:Form` (for token frequency, etc.), `ontolex:LexicalEntry` (frequency of disambiguated lemmas), `ontolex:LexicalSense` (sense frequency), `ontolex:LexicalConcept` (e.g., synset frequency), `lexicog:Entry` (if used for representing homonyms: frequency of non-disambiguated lemmas), etc. (cf. Fig. 1). 
In particular, we consider all these elements as being countable, annotatable/attestable and suitable for a numerical representation by means of an embedding. For this reason, we introduce `frac:Observable` as a top-level element within the FrAC module that is used to define the `rdfs:domain` of any properties that link lexical and corpus-derived information. 

> **Note:** The definition `frac:Observable` does not posit an exhaustive list of possible observables. Instead, anything that can be observed in a corpus can be defined as `frac:Observable`. This includes elements of OntoLex modules not listed here (e.g., `decomp:Component`, `synsem:SyntacticArgument`, etc.) or future OntoLex vocabularies. Likewise, it can also include URIs which have no relation to OntoLex whatsoever, as these are foreseen as external elements that OntoLex-Lemon can provide information about, but only if they are based on or linked with corpus information, attested in a document, a text or its annotations.

<section class="entity">
#### Observation (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Observation](http://www.w3.org/ns/lemon/frac#Observation)

**Observation** is an abstract superclass for anything that can be observed in a corpus about an Observable. An observation MUST have at least one `rdf:value` to express its value, it SHOULD have exactly one `frac:observedIn` property that defines the data from which this information was drawn, and it SHOULD have a `dct:description` explaining the methodolgy and/or extraction method by which the observation was obtained.

<div class="description">
**SubClassOf:** exactly 1 `frac:observedIn`, min 1 `dct:description`, exactly 1 rdf:value
</div>
</section>

Observations as understood here are **empirical** (quantitative) observations that are made against a corpus, a text, a document or another type of language data. Observations can be made in any  kind  of  (collection  or excerpt of)  linguistic  data  at  any scale,  structured  or  unstructured, regardless of its physical materialization (as an electronic corpus, as a series of printed books, as a bibliographical database or as metadata record for a particular corpus).

<section class="entity">
#### observedIn (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#observedIn](http://www.w3.org/ns/lemon/frac#Observation)

For a `frac:Observation`,  the property **observedIn** defines the URI of the data source (or its metadata entry) that this particular observation was made in or derived from. This can be, for example, a corpus or a text represented by its access URL, a book represented by its bibliographical metadata, etc.

As these data sources can have different characteristics, users SHOULD specify their respective type using the [DCMI Type Vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7).

<div class="description">
**Domain:** frac:Observation

**Range:** anyURI
</div>
</section>

For machine-readable corpora that are/can be characterized by their size, data providers can provide overall size information using the property `frac:total`, see section on Frequency below.

</section>

<section id="frequency">

## Frequency

Frequency information is a crucial component in human language technology. Corpus-based lexicography originates with Francis and Kucera (1958), and subsequently, the analysis of frequency distributions of word forms, lemmas and other linguistic elements has become a standard technique in lexicography and philology, and given rise to the field of corpus linguistics. At its core, this means that lexicographers use (corpus) frequency and distribution information while compiling lexical entries (also see the section on collocations and similarity below). As a qualitative assessment, frequency can be expressed with [lexinfo:frequency](http://www.lexinfo.net/ontology/2.0/lexinfo#frequency), "[t]he relative commonness with which a term occurs". However, this is an object property with possible values lexinfo:commonlyUsed, lexinfo:infrequentlyUsed, lexinfo:rarelyUsed, while absolute counts over a particular resource (corpus) require novel vocabulary elements.

For modelling, we focus on absolute frequencies, as relative frequencies can be derived if absolute frequencies and totals are known. Absolute frequencies are used in computational lexicography (e.g., the [Electronic Penn Sumerian Dictionary](http://oracc.museum.upenn.edu/epsd2/)), and they are an essential piece of information for NLP and corpus linguistics.
In order to avoid confusion with lexinfo:Frequency (which provides lexicographic assessments such as commonly used, infrequently used, etc.), this is defined with reference to a particular dataset, a corpus.

<div class="entity">
#### Frequency (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Frequency](http://www.w3.org/ns/lemon/frac#Frequency)

**Frequency** is a `frac:Observation` of the absolute number of attestations (`rdf:value`) of a particular `frac:Observable` (see `frac:frequency`) that is `frac:observedIn` in a particular data source. Using `frac:unit`, frequency objects can also identify the (segmentation) unit that their counts are based on. 
<div class="description">
**SubClassOf:** `frac:Observation`
 **SubClassOf:** `rdf:value` exactly 1 , `frac:observedIn` exactly 1
</div>
</div>

</section>



