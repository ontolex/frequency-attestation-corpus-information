---
title: The Ontolex Module for Frequency, Attestation and Corpus Information
editor:
- name: Christian Chiarcos
  companyURL: https://www.uni-augsburg.de/de/fakultaet/philhist/professuren/angewandte-computerlinguistik/
  company: Applied Computational Linguistics, University of Augsburg, Germany
- name: John P. McCrae
  companyURL: https://www.universityofgalway.ie/
  company: University of Galway
author:
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

<div class="entity">

Observable (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Observable](http://www.w3.org/ns/lemon/frac#Observable)

**Observable** is an abstract superclass for any element of a lexical resource that frequency, attestation or corpus-derived information can be expressed about. This includes, among others, `ontolex:LexicalEntry`, `ontolex:LexicalSense`, `ontolex:Form`, and `ontolex:LexicalConcept`. Elements that FrAC properties apply to  must be observable in a corpus or another linguistic data source.
</div>

</div>

<figure>

![](img/ontolex-element.png "frac:Observable")

<figcaption>`frac:Observable` as a superclass of ontolex:LexicalEntry, ontolex:Form, ontolex:LexicalSense and ontolex:LexicalConcept</figcaption>

</figure>

For OntoLex, we assume that frequency, attestation and corpus information can be provided about _every_ linguistic content element in the OntoLex-Lemon core model and in existing or forthcoming OntoLex modules. This includes `ontolex:Form` (for token frequency, etc.), `ontolex:LexicalEntry` (frequency of disambiguated lemmas), `ontolex:LexicalSense` (sense frequency), `ontolex:LexicalConcept` (e.g., synset frequency), `lexicog:Entry` (if used for representing homonyms: frequency of non-disambiguated lemmas), etc. (cf. Fig. 1). 
In particular, we consider all these elements as being countable, annotatable/attestable and suitable for a numerical representation by means of an embedding. For this reason, we introduce `frac:Observable` as a top-level element within the FrAC module that is used to define the `rdfs:domain` of any properties that link lexical and corpus-derived information. 

> **Note:** The definition `frac:Observable` does not posit an exhaustive list of possible observables. Instead, anything that can be observed in a corpus can be defined as `frac:Observable`. This includes elements of OntoLex modules not listed here (e.g., `decomp:Component`, `synsem:SyntacticArgument`, etc.) or future OntoLex vocabularies. Likewise, it can also include URIs which have no relation to OntoLex whatsoever, as these are foreseen as external elements that OntoLex-Lemon can provide information about, but only if they are based on or linked with corpus information, attested in a document, a text or its annotations.

<div class="entity">

Observation (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Observation](http://www.w3.org/ns/lemon/frac#Observation)

**Observation** is an abstract superclass for anything that can be observed in a corpus about an Observable. An observation MUST have at least one `rdf:value` to express its value, it SHOULD have exactly one `frac:observedIn` property that defines the data from which this information was drawn, and it SHOULD have a `dct:description` explaining the methodolgy and/or extraction method by which the observation was obtained.

<div class="description">

**SubClassOf:** exactly 1 `frac:observedIn`, min 1 `dct:description`, exactly 1 rdf:value

</div>

</div>

Observations as understood here are **empirical** (quantitative) observations that are made against a corpus, a text, a document or another type of language data. Observations can be made in any  kind  of  (collection  or excerpt of)  linguistic  data  at  any scale,  structured  or  unstructured, regardless of its physical materialization (as an electronic corpus, as a series of printed books, as a bibliographical database or as metadata record for a particular corpus).

<div class="entity">

observedIn (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#observedIn](http://www.w3.org/ns/lemon/frac#Observation)

For a `frac:Observation`,  the property **observedIn** defines the URI of the data source (or its metadata entry) that this particular observation was made in or derived from. This can be, for example, a corpus or a text represented by its access URL, a book represented by its bibliographical metadata, etc.

As these data sources can have different characteristics, users SHOULD specify their respective type using the [DCMI Type Vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7).

<div class="description">

**Domain:** frac:Observation

**Range:** anyURI

</div>
</div>

For machine-readable corpora that are/can be characterized by their size, data providers can provide overall size information using the property `frac:total`, see section on Frequency below.

</section>

<section id="frequency">

## Frequency

Lexicographers use (corpus) frequency and distribution information while compiling lexical entries, as a qualitative assessment of their resources. In this module, we focus on absolute frequencies, as relative frequencies can be derived if absolute frequencies and totals are known. Absolute frequencies are used in computational lexicography, and they are an essential piece of information for NLP and corpus linguistics.

<div class="entity">

Frequency (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Frequency](http://www.w3.org/ns/lemon/frac#Frequency)

**Frequency** is a `frac:Observation` of the absolute number of attestations (`rdf:value`) of a particular `frac:Observable` (see `frac:frequency`) that is `frac:observedIn` in a particular data source. Using `frac:unit`, frequency objects can also identify the (segmentation) unit that their counts are based on. 
<div class="description">

**SubClassOf:** `frac:Observation`

**SubClassOf:** `rdf:value` exactly 1 , `frac:observedIn` exactly 1

</div>
</div>

<div class="entity">

unit (Property)

**URI:** [http://www.w3.org/ns/lemon/frac#unit](http://www.w3.org/ns/lemon/frac#unit)

For a `frac:Frequency` object, the property **unit** provides an identifier of the respective segmentation unit.

<div class="description">

**rdfs:range** `frac:Frequency`

</div>
</div>

Examples for `frac:unit` include string literals such as `"tokens"`, `"sentences"`, etc. If a future community standard provides reference URIs for such datatypes, `frac:unit` should be used as a datatype property. Until such a convention has been established, it is recommended to be used as a datatype property.

> Note: One function of `frac:unit` is to calculate relative frequencies from absolute values as provided by the `rdf:value` of `frac:Frequency` objects. While these can be calculated by diving `rdf:value` of a particular frequency object *f* by the `rdf:value` of its `frac:observedIn/frac:total`, this equation is restricted to frequency objects using the same `frac:unit`.

<div class="entity">

frequency (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#frequency](http://www.w3.org/ns/lemon/frac#frequency)

The property **frequency** assigns a particular `frac:Observable` a `frac:Frequency`.

<div class="description">

**rdfs:domain** `frac:Observable`

**rdfs:range** `frac:Frequency`
</div>
</div>

<div class="note">

If information from multiple language resources is aggregated (also cf. the section on embeddings below), these should be aggregated into a a single data source that can be referred to by `frac:observedIn`, as there must be exactly one `frac:observedIn`.

</div>

The definition above only applies to absolute frequencies. For expressing relative frequencies, we  expect  the associated data source (`frac:observedIn`) object to  define  a  total  of  elements  contained  (`frac:total`). In many practical applications, it is necessary to provide relative  counts,  and  in  this  way,  these  can  be  easily  derived  from  the  absolute  (element)  frequency  provided  by the Frequency class  and  the  total  defined  by the underlying  corpus. If the real absolute values are unknown and only relative scores are provided, data providers should use percentage values for both the `Frequency` `rdf:value` and for the `frac:total` (i.e., `100%`) of the associated corpus.

<div class="entity">

total (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#total](http://www.w3.org/ns/lemon/frac#total)

The object property **total** assigns  any potential FrAC data source (i.e., `dct:Collection`, `dct:Dataset`, `dct:Text` or any other member of DCMI Type) the  total  number  of  elements  that  it  contains as a `frac:Frequency` object.

<div class="description">

**Domain:** class that is a `dcam:memberOf` DCMI Type

**Range:** frac:Frequency
</div>
</div>

<div class="note">

For `frac:total`, users should provide both the frequency and the segmentation/unit over which this frequency is obtailed. For an observable, then, relative frequencies (for any given unit *u*) can then be calculated from the object values of `frac:frequency/rdf:value`  and `frac:frequency/frac:observedIn/frac:total/rdf:value` if (and only if) the correspondung units match.

</div>

The following example illustrates word and form frequencies for the Sumerian word _a_ (n.) "water" from the [Electronic Penn Sumerian Dictionary](http://oracc.museum.upenn.edu/epsd2/sux) and the frequencies of the underlying corpus.

<aside class="example" title="Example: Frequency of the Sumerian word _a_ 'water'">

```turtle
# word frequency, over all form variants 
epsd:kalag_strong_v a ontolex:LexicalEntry;
    frac:frequency [
        a frac:Frequency; 
        rdf:value "2398"^^xsd:int; 
        frac:observedIn <http://oracc.museum.upenn.edu/epsd2/pager>
    ] .

# form frequency for individual orthographical variants 
epsd:kalag_strong_v ontolex:canonicalForm [
    ontolex:writtenRep "kal-ga"@sux-Latn; 
    frac:frequency [
        a frac:Frequency; 
        rdf:value "2312"^^xsd:int; 
        frac:observedIn <http://oracc.museum.upenn.edu/epsd2/pager>
        ]
    ] .

epsd:kalag_strong_v ontolex:otherForm [ 
    ontolex:writtenRep "kalag"@sux-Latn; 
    frac:frequency [ 
        a frac:Frequency; 
        rdf:value "70"^^xsd:int; 
        frac:observedIn <http://oracc.museum.upenn.edu/epsd2/pager>
        ]
    ] .
```

</aside>

The example shows orthographic variation (in the original writing system, Sumerian Cuneiform sux-Xsux, and its Latin transcription sux-Latn). It is slightly simplified insofar as the ePSD2 provides individual counts for different periods and that only three of six orthographical variants are given. Note that these are orthographical variants, not morphological variants (which are not given in the dictionary).

<div class="note">
TODO: update the examples below with explicit `Corpus` elements. Add total.
</div>
</section>

<section id="Attestion">

## Attestation

Attestations constitute  a  special  form  of  citation  that  provide  evidence  for  the  existence  of  a  certain  lexical  phenomena; they can elucidate meaning or illustrate various  linguistic  features.

In  scholarly  dictionaries,  attestations  are  a  representative selection  from  the  occurrences  of  a  headword  in  a  textual corpus.  These  citations  often  consist  of  a quotation  accompanied  by  a  reference  to  the  source.  The  quoted  text  usually contains  the  occurrence  of  the  headword.

<div class="entity">

Attestation (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Attestation](http://www.w3.org/ns/lemon/frac#Attestation)

An **Attestation** is a `frac:Observation` that represents one exact or normalized quotation  or  excerpt  from  a  source  document  that  illustrates a  particular  form,  sense,  lexeme  or  features  such  as  spelling variation,  morphology,  syntax,  collocation,  register.  An attestation SHOULD have an `rdf:value`, it CAN have a `frac:gloss`, and it SHOULD have a `frac:observedIn` or `frac:locus` object to identify the source of this material.
For an attestation, `rdf:value` represents the text of a quotation as represented in the original source. If that needs to be distinguished or is different from the way how it is represented in the dictionary, FrAC users should use `frac:gloss` for the latter purpose. 

<div class="description">

**SubClassOf:** `rdf:value` max 1 

**SubClassOf:** `frac:Observation`
</div>
</div>

<div class="entity">

attestation (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#attestation](http://www.w3.org/ns/lemon/frac#attestation)

The property **frac:attestation** associates an attestation to the frac:Observable.  This  is  a  subproperty  of  `frac:citation` using concrete data as  evidence.

<div class="description">

**Domain:** `Observable`

**Range:** `Attestation`

**SubPropertyOf:** `citation`
</div>
</div>

<div class="entity">

citation (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#citation](http://www.w3.org/ns/lemon/frac#citation)

The property **frac:citation** associates a  citation  to  the  `Observable`  citing  it.

<div class="description">

**Domain:**  `Observable`
</div>
</div>

In general, the object of a citation represents the successful act of citing an entity which can be referred to by a standardised bibliographic reference, cf. Peroni (2012) \cite{peroni2012fabio}: 

> [a Citation is] “a conceptual directional link from a citing entity to a cited entity, created by a human performative act of making a citation, typically instantiated by the inclusion of a bibliographic reference  in the reference list of the citing entity, or by the inclusion within the citing entity of a link, in the form of an HTTP Uniform Resource Locator (URL), to a resource on the World Wide Web”.

However, note that FrAC does not formally define a general "Citation" class to define the range of `citation`, but only provides `Attestation` as one specific possibility. Beyond attestations, different vocabularies have been suggested for linking bibliographical information, and we advise users of FrAC to make a consistent choice among them, adequate for their respective needs and the conventions of their users community. `frac:citation` serves as an interface to these external vocabularies. If the [CITO vocabulary](https://sparontologies.github.io/cito/current/cito.html) is used in a particular resource, their FrAC Citations can be defined as the subclass of CITO citations having <tt>frac:Observable</tt> as citing entity and attestations would correspond to citations with the <tt>cito:hasCitationCharacterization</tt> value <tt>citesAsEvidence</tt>. Other relevant vocabularies include, for example, [BIBFRAME](https://www.loc.gov/bibframe/), [FRBR](https://www.ifla.org/node/881) and [FaBiO](https://sparontologies.github.io/fabio/current/fabio.html), but also, generic vocabularies such as [schema.org](https://schema.org/citation).

<div class="entity">

gloss (Property)

**URI:** [http://www.w3.org/ns/lemon/frac#gloss](http://www.w3.org/ns/lemon/frac#gloss)

The **gloss** of an attestation contains  the  text  content  of  an  attestation  *as  represented  within  a  dictionary*.  This property should not be used to provide direct quotations from the original data source, which should be represented by `rdf:value`. Instead, its recommended use is for representations that are either enriched (e.g., by annotations and metadata), amended (e.g., by expanding ligatures or omissions), simplified (e.g., by omissions from the original context, e.g., of the lexeme under consideration) or otherwise differentiated from the plain text representation of the context.

<div class="description">

**Domain:** `Attestation`

**Range:** `xsd:String`  
</div>
</div>

<div class="note">
With `frac:gloss` and `rdf:value`, `frac:Attestation` provides *two* different properties to represent the context of an observable in any particular data source. `rdf:value` should provide information as found in the underlying corpus, e.g., a plain text string. If the dictionary provides a different representation, or if the attestation as given in an underlying dictionary has not yet been confirmed to match the context in the underlying corpus, applications should use `frac:gloss` instead of `rdf:value`. In other words, `rdf:value` corresponds to the representation of the context in the underlying corpus, `frac:gloss` to its representation in the underlying dictionary. If both are confirmed to be equal, use `rdf:value`.
</div>

As an example, for Old English *hwæt-hweganunges*, Bosworth (2014) gives the example `"Ða niétenu ðonne beóþ hwæthuguningas [MS. Cote. -hwugununges] ...`. In OntoLex-FrAC, this would be the `frac:gloss` because it contains additional information about spelling variation/normalized spelling not found found in the quoted source (`MS. Cote.`):

<aside class="example" title="Example: Attestation of Old English *hwæt-hweganunges*">

```turtle
<https://bosworthtoller.com/20070> a ontolex:LexicalEntry;
    frac:attestation [
        a frac:Attestation;
        rdf:value "Ða niétenu ðonne beóþ hwæthwugununges" ;
        frac:gloss "Ða niétenu ðonne beóþ hwæthuguningas [MS. Cote. -hwugununges] ..."
        # TODO: resolve literature pointers properly!
    ] .
```

<div class="note">
 Bosworth, Joseph. “hwæt-hweganunges.” In _An Anglo-Saxon Dictionary Online_, edited by Thomas Northcote Toller, Christ Sean, and Ondřej Tichy. Prague: Faculty of Arts, Charles University, 2014. https://bosworthtoller.com/20070. [REFORMAT]
 </div>
 </aside>

In many applications, it is desirable to specify the location of the occurrence of a headword in the quoted text of an attestation, for example, by means of character offsets. Different conventions for referencing strings by character offsets do exist, representative solutions are string URIs as provided by RCF5147 (for plain text) and NIF (all mimetypes), As different vocabularies can be used to establish locus objects, the FrAC vocabulary is underspecified with respect to the exact nature of the locus object. Accordingly, the <tt>locus</tt> property that links an attestation with its source takes any URI as object.

<div class="entity">

locus (ObjectProperty)

**URI:** [http://www.w3.org/ns/lemon/frac#locus](http://www.w3.org/ns/lemon/frac#locus)

**frac:locus** points  to  the  location  at  which  the  relevant  word(s)  can  be  found.

<div class="description">

**Domain:** `Attestation`
</div>
</div>

<div class="note">
In humanities practice, locations (`frac:locus` objects) can be provided at different levels of granularity, e.g., referring to a particular text span within a text, to a verse, paragraph or chapter within which the text can be found, to a complete work, or a collection of works. Data providers should generally use `frac:observedIn` unless the the specific semantics require the use of `frac:locus`. In particular, if the location is a complete work (e.g., `dct:Text`) or a corpus identifiable by a URI (i.e., a `dct:Collection`), data providers should use the `frac:observedIn` property. For references within a work or to a collection without explicitly defined boundaries (e.g., `Plato` to designate all of Plato's preserved works as well as any statement ascribed to him from an unpreserved work), data providers should use `frac:locus`.
</div>

<div class="note">
Implementation note: as the type of data source is now to indicated by `dct:DMCIType`, we can merge `frac:locus` and `frac:observedIn`, again.
</div>

<aside class="example" title="Example: DiaMaNT">

[DiaMaNT (_Diachroon seMAntisch lexicon van de Nederlandse Taal_)](http://diamant.ivdnt.org/diamant-ui/) is a diachronic semantic computational  lexicon  of  Dutch,  at its core  formed by four scholarly historical dictionaries of  Dutch covering a language period from ca. 500 –  1976. The example below illustrates the combination of FrAC attestations with the [CITO](https://sparontologies.github.io/cito/current/cito.html) and [FRBR](http://purl.org/vocab/frbr/core#) vocabularies, as well as with the [NLP Interchange Format](https://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core/nif-core.html).

```turtle
diamant:entry_WNT_M030758 a ontolex:LexicalEntry ; 
    ontolex:sense diamant:sense_WNT_M030758_bet_207 .

diamant:sense_WNT_M030758_bet_207 a ontolex:LexicalSense;
    rdfs:label "V.-" ;
frac:attestation diamant:attestation_2108540 ; 
skos:definition "Iemand een kat (of de kat) aan het  been  jagen...... iemand in moeilijkheden brengen." .

diamant:attestation_2108540 a frac:Attestation ; 
    cito:hasCitedEntity diamant:cited_document_WNT_332819  ;
    cito:hasCitingEntity diamant:sense_WNT_M030758_bet_207; 
    frac:locus diamant:locus_2108540  ;
    frac:quotation "... dat men licht yemant de cat aen het been kan werpen," .

diamant:locus_2108540 a diamant:Occurrence ; 
    nif:beginIndex 107 ;
    nif:endIndex 110 .

diamant:cited_document_WNT_332819 a frbr:Manifestation ;
    frbr:embodimentOf diamant:expression_WNT_332819 ; 
    diamant:witnessYearFrom 1621 ;
    diamant:witnessYearTo 1621 .

diamant:expression_WNT_332819 a frbr:Expression ; 
    dcterms:creator "N. V. REIGERSB." ; 
    dcterms:title "Brieven van Nicolaes van Reigersberch aan Hugo de Groot" ; 
    frbr:embodiment diamant:quotation_WNT_332819 .
```
</aside>

<div class="note">
In the example above, NIF is not correctly used: NIF requires string URIs for loci, including the identification of the source document within the base URI and the identification of a context (this is instead provided via `hasCitedEntity`). To be revised or replaced.
</div>

<div class="note">
Update example to https://www.dbnl.org/tekst/groo001brie04_01/groo001brie04_01_0003.php?q=dat%20men%20licht%20yemant%20de%20cat%20aen%20het%20been%20kan%20werpen;#hl1
</div>

</section>

<section id="collocations">

## Collocations

Collocation analysis is an important tool for lexicographical research and instrumental for modern NLP techniques. It has been the mainstay of 1990s corpus linguistics and continues to be an area of active research in computational philology and lexicography.

Collocations are usually defined on surface-oriented criteria, i.e., as a relation between forms or lemmas (lexical entries), not between senses, but they can be analyzed on the level of word senses (the sense that gave rise to the idiom or collocation). Indeed, collocations often contain a variable part, which can be represented by a <tt>ontolex:LexicalConcept</tt>.

Collocations can involve two or more words, they are thus modelled as an <tt>rdfs:Container</tt> of <tt>frac:Observables</tt>s. Collocations may have a fixed or a variable word order. Where fixed word order is required, the collocation must be defined as a sequence (<tt>rdf:Seq</tt>), otherwise, the default interpretation is as an ordered set (<tt>rdf:Bag</tt>).

Collocations obtained by quantitative methods are characterized by their method of creation (<tt>dct:description</tt>), their collocation strength (<tt>rdf:value</tt>), and the corpus or data source used to create them (<tt>frac:observedIn</tt>). Collocations share these characteristics with other `frac:Observation`s and thus, these are inherited from the abstract <tt>frac:Observation</tt> class.


<div class="entity">

Collocation (Class)

**URI:** [http://www.w3.org/ns/lemon/frac#Collocation](http://www.w3.org/ns/lemon/frac#Collocation)

A **Collocation** is a <tt>frac:Observation</tt> that describes the co-occurrence of two or more <tt>frac:Observables</tt>s within the same context window and that can be characterized by their collocation score (or weight, <tt>frac:cScore</tt>) in a particular data source (<tt>frac:observedIn</tt>). Collocations are both observations and observables, and they are modelled as an aggregate (`rdfs:Container`) of observables.

<div class="description">

**SubClassOf:** <tt>frac:Observation, rdfs:Container, frac:Observable</tt>

**rdfs:member:** only <tt>frac:Observable</tt>

**SubClassOf:** `frac:head` max 1
</div>
</div>

Collocations are collections of `frac:Observables`, and formalized as <tt>rdfs:Container</tt>, i.e., <tt>rdf:Seq</tt> or <tt>rdf:Bag</tt>. The elements of any collocation can be accessed by `rdfs:member`. In addition, the elements of an ordered collocation (`rdfs:subClassOf rdf:Seq`) can be accessed by means of numerical indices (`rdf:_1`, `rdf:_2`, etc.). 
    
By default, <tt>frac:Collocation</tt> is insensitive to word order. If a collocation is word order sensitive, it should be defined as `rdfs:subClassOf rdf:Seq`. Collocation analysis typically involves additional parameters such as the size of the context window considered. Such information can be provided in human-readable form in <tt>dct:description</tt>. 

<div class="note">
Note that FrAC collocations can be used to represent collocations both in the lexicographic sense (as complex units of meaning) and in the quantative sense (as determined by collocation metrics over a particular corpus), but that the quantitative interpretation is the preferred one in the context of FrAC. To mark collocations in the lexicographic sense as such, they can be assigned a corresponding `lexinfo:termType`, e.g., by means of `lexinfo:idiom`, `lexinfo:phraseologicalUnit` or `lexinfo:setPhrase`. If explicit sense information is being provided, the recommended modelling is by means of `ontolex:MultiWordExpression` and the OntoLex-Decomp module rather than `frac:Collocation`. To provide collocation scores about a `ontolex:MultiWordExpression`, it can be linked via `rdfs:member` with a `frac:Collocation`.
</div>
    
Collocations are `frac:Observable`s, i.e., they can be ascribed `frac:frequency`, `frac:attestation`, `frac:embedding`, they can be described in terms of their (embedding) similarity, and they can be nested inside larger collocations.
    
Collocations can be described in terms of various collocation scores. If scores for multiple metrics are being provided, these should not use the generic `rdf:value` property, but a designated subproperty of `frac:cScore`:

<div class="entity">
cScore (property)

*URI:** [http://www.w3.org/ns/lemon/frac#cScore](http://www.w3.org/ns/lemon/frac#cScore)

**Collocation score** is a subproperty of `rdf:value` that provides the value for one specific type of collocation score for a particular collocation in its respective corpus. Note that this property should not be used directly, but instead, its respective sub-properties for scores of a particular type.

<div class="description">

**SubPropertyOf:** <tt>rdf:value</tt>

**domain:** <tt>frac:Collocation</tt>
</div>
</div>

LexInfo defines a number of popular collocation metrics as sub-properties of `frac:cScore`:

- `lexinfo:relFreq` (*relative frequency*): <math><mrow><mi>R</mi><mi>F</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mi>|</mi><mi>x</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mfrac><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><msub><mi>f</mi><mi>x</mi></msub></mfrac><mo form="prefix" stretchy="false">(</mo><mo>=</mo><msub><mi>R</mi><mi>x</mi></msub><mo form="postfix" stretchy="false">)</mo></mrow></math> (asymmetric, requires `frac:head`)
- `lexinfo:pmi` (*pointwise mutual information*, sometimes referred to as *MI-score* or *association ratio*, cf. [Church and Hanks 1990, via Ewert 2005](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf): <math><mrow><mi>P</mi><mi>M</mi><mi>I</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mi>l</mi><mi>o</mi><msub><mi>g</mi><mn>2</mn></msub><mfrac><mrow><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><mi>N</mi></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><msub><mi>f</mi><mi>y</mi></msub></mrow></mfrac></mrow></math>
- `lexinfo:pmi2` (*PMI²-score*): <math><mrow><mi>P</mi><mi>M</mi><msup><mi>I</mi><mn>2</mn></msup><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mi>l</mi><mi>o</mi><msub><mi>g</mi><mn>2</mn></msub><mfrac><mrow><msubsup><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow><mn>2</mn></msubsup><mi>N</mi></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><msub><mi>f</mi><mi>y</mi></msub></mrow></mfrac></mrow></math>
- `lexinfo:pmi3` (*PMI³-score*, cf. [Daille 1994 in Ebert 2005, p.89](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf)): <math><mrow><mi>P</mi><mi>M</mi><msup><mi>I</mi><mn>3</mn></msup><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mi>l</mi><mi>o</mi><msub><mi>g</mi><mn>2</mn></msub><mfrac><mrow><msubsup><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow><mn>3</mn></msubsup><mi>N</mi></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><msub><mi>f</mi><mi>y</mi></msub></mrow></mfrac></mrow></math>
- `lexinfo:pmiLogFreq` (*PMI.log-f*, *salience*, formerly default metric in SketchEngine): <math><mrow><mi>P</mi><mi>M</mi><mi>I</mi><mi>.</mi><mi>l</mi><mi>o</mi><mi>g</mi><mo>−</mo><mi>f</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mi>l</mi><mi>o</mi><msub><mi>g</mi><mn>2</mn></msub><mfrac><mrow><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><mi>N</mi></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><msub><mi>f</mi><mi>y</mi></msub></mrow></mfrac><mo>×</mo><mi>l</mi><mi>o</mi><mi>g</mi><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow></math>
- `lexinfo:dice` (*Dice coefficient*): <math><mrow><mi>D</mi><mi>i</mi><mi>c</mi><mi>e</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mfrac><mrow><mn>2</mn><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><mo>∪</mo><msub><mi>f</mi><mi>y</mi></msub></mrow></mfrac></mrow></math>
- `lexinfo:logDice` (default metric in SketchEngine, [Rychly 2008](https://www.sketchengine.eu/wp-content/uploads/2015/03/Lexicographer-Friendly_2008.pdf)): <math><mrow><mi>L</mi><mi>o</mi><mi>g</mi><mi>D</mi><mi>i</mi><mi>c</mi><mi>e</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo><mi>l</mi><mi>o</mi><msub><mi>g</mi><mn>2</mn></msub><mi>D</mi><mi>i</mi><mi>c</mi><mi>e</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo></mrow></math>
- `lexinfo:minSensitivity` (*minimum sensitivity*, cf. [Pedersen 1998](https://www.sketchengine.eu/wp-content/uploads/ske-statistics.pdf)): <math><mrow><mi>M</mi><mi>S</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mi>m</mi><mi>i</mi><mi>n</mi><mo form="prefix" stretchy="false">(</mo><msub><mi>R</mi><mi>x</mi></msub><mo separator="true">,</mo><msub><mi>R</mi><mi>y</mi></msub><mo form="postfix" stretchy="false">)</mo></mrow></math>

with
    
- <math><mrow><mi>x</mi><mo separator="true">,</mo></mrow><mrow><mi>y</mi></mrow></math> the (head) word and its collocate
- <math><msub><mi>f</mi><mi>x</mi></msub></math> the number of occurrences of the word *x*
- <math><msub><mi>f</mi><mi>y</mi></msub></math> the number of occurrences of the word *y*
- <math><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></math> the number of co-occurrences of the words *x* and *y*
- <math><mrow><msub><mi>R</mi><mi>y</mi></msub><mo>=</mo></mrow><mrow><mfrac><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><msub><mi>f</mi><mi>y</mi></msub></mfrac></mrow></math> relative frequency of *y*
- <math><mi>N</mi></math> the total number of words in the corpus, this should be documented in `dct:description`

In addition to collocation scores, also statistical independence tests are being employed as collocation scores:

- `lexinfo:logLikelihood` (*log likelihood*, *G²* [Dunning 1993, via Ewer 2005](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf))
- `lexinfo:tScore` (*Student's t test*, *T-score*, cf. [Church et al. 1991, via Ewert 2005, p.82](https://elib.uni-stuttgart.de/bitstream/11682/2573/1/Evert2005phd.pdf) ): <math><mrow><mi>T</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mfrac><mrow><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><mo>−</mo><mfrac><mrow><mo form="prefix" stretchy="false" lspace="0em" rspace="0em">(</mo><msub><mi>f</mi><mi>x</mi></msub><msub><mi>f</mi><mi>y</mi></msub><mo form="postfix" stretchy="false" lspace="0em" rspace="0em">)</mo></mrow><mi>N</mi></mfrac></mrow><msqrt><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></msqrt></mfrac></mrow></math>
- `lexinfo:chi2` (*Person's Chi-square test* [Manning 1999](https://nlp.stanford.edu/fsnlp/) ): <math><mrow><msup><mi>χ</mi><mn>2</mn></msup><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mfrac><mrow><mi>N</mi><mo form="prefix" stretchy="false">(</mo><msub><mi>O</mi><mn>11</mn></msub><msub><mi>O</mi><mn>22</mn></msub><mo>−</mo><msub><mi>O</mi><mn>12</mn></msub><msub><mi>O</mi><mn>21</mn></msub><msup><mo form="postfix" stretchy="false">)</mo><mn>2</mn></msup></mrow><mrow><mo form="prefix" stretchy="false" lspace="0em" rspace="0em">(</mo><msub><mi>O</mi><mn>11</mn></msub><mo>∪</mo><msub><mi>O</mi><mn>12</mn></msub><mo form="postfix" stretchy="false">)</mo><mo form="prefix" stretchy="false">(</mo><msub><mi>O</mi><mn>11</mn></msub><mo>∪</mo><msub><mi>O</mi><mn>21</mn></msub><mo form="postfix" stretchy="false">)</mo><mo form="prefix" stretchy="false">(</mo><msub><mi>O</mi><mn>12</mn></msub><mo>∪</mo><msub><mi>O</mi><mn>22</mn></msub><mo form="postfix" stretchy="false">)</mo><mo form="prefix" stretchy="false">(</mo><msub><mi>O</mi><mn>21</mn></msub><mo>∪</mo><msub><mi>O</mi><mn>22</mn></msub><mo form="postfix" stretchy="false" lspace="0em" rspace="0em">)</mo></mrow></mfrac></mrow></math>

with

- <math><mrow><msub><mi>O</mi><mn>11</mn></msub><mo>=</mo></mrow><mrow><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow></math>
- <math><mrow><msub><mi>O</mi><mn>12</mn></msub><mo>=</mo></mrow><mrow><msub><mi>f</mi><mi>y</mi></msub><mo>−</mo></mrow><mrow><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow></math>
- <math><mrow><msub><mi>O</mi><mn>21</mn></msub><mo>=</mo></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><mo>−</mo></mrow><mrow><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow></math>
- <math><mrow><msub><mi>O</mi><mn>22</mn></msub><mo>=</mo></mrow><mrow><mi>N</mi><mo>−</mo></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><mo>−</mo></mrow><mrow><msub><mi>f</mi><mi>y</mi></msub><mo>∪</mo></mrow><mrow><mn>2</mn><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow></math>
- <math><mi>N</mi></math> -  the total number of words in the corpus 
    
In addition to classical collocation metrics as established in computational lexicography and corpus linguistics, related metrics can also be found in different disciplines and are represented here as subproperties of frac:cScore, as well. This includes metrics for association rule mining. In this context, an association  rule (collocation) <math><mrow><mi>x</mi><mo stretchy="false">→</mo></mrow><mrow><mi>y</mi></mrow></math> means that the existence of word *x* implies the existence of word *y* 

- `lexinfo:support` (the *support* is an indication of how frequently the rule appears in the dataset): <math><mrow><mi>s</mi><mi>u</mi><mi>p</mi><mi>p</mi><mi>o</mi><mi>r</mi><mi>t</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo stretchy="false">→</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mfrac><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><mi>N</mi></mfrac></mrow></math> (with *N* the total number of collocations)
- `lexinfo:confidence` (the *confidence* is an indication of how often the rule has been found to be true): <math><mrow><mi>c</mi><mi>o</mi><mi>n</mi><mi>f</mi><mi>i</mi><mi>d</mi><mi>e</mi><mi>n</mi><mi>c</mi><mi>e</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo stretchy="false">→</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mfrac><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><msub><mi>f</mi><mi>x</mi></msub></mfrac></mrow></math>
- `lexinfo:lift` (the *lift* or *interest* of a rule measures how many times more often *x* and *y* occur together than expected if they are statistically independent): <math><mrow><mi>l</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo stretchy="false">→</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mfrac><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub><mrow><msub><mi>f</mi><mi>x</mi></msub><msub><mi>f</mi><mi>y</mi></msub></mrow></mfrac></mrow></math>
- `lexinfo:conviction` (the *conviction* of a rule is interpreted as the ratio of the expected frequency that *x* occurs without *y*, i.e., the frequency that the rule makes an incorrect prediction, if *x* and *y* are independent divided by the observed frequency of incorrect predictions): <math><mrow><mi>c</mi><mi>o</mi><mi>n</mi><mi>v</mi><mi>i</mi><mi>c</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mo form="prefix" stretchy="false">(</mo><mi>x</mi><mo stretchy="false">→</mo><mi>y</mi><mo form="postfix" stretchy="false">)</mo><mo>=</mo></mrow><mrow><mfrac><mrow><mo form="prefix" stretchy="false" lspace="0em" rspace="0em">(</mo><mn>1</mn><mo>−</mo><msub><mi>f</mi><mi>y</mi></msub><mo form="postfix" stretchy="false">)</mo><msub><mi>f</mi><mi>x</mi></msub></mrow><mrow><msub><mi>f</mi><mi>x</mi></msub><mo>−</mo><msub><mi>f</mi><mrow><mi>x</mi><mi>y</mi></mrow></msub></mrow></mfrac></mrow></math>
 
 <div class="note">
As OntoLex does not provide a generic inventory for grammatical relations, scores defined for grammatical relations are omitted (cf. https://www.sketchengine.eu/wp-content/uploads/ske-statistics.pdf). However, these may be defined by the user.
</div>
    
Many of these metrics are asymmetric and distinguish the lexical element they are about (the head) from its collocate(s). If such metrics are provided, a collocation should explicitly identify its head:


<div class="entity">
head (property)

**URI:** [http://www.w3.org/ns/lemon/frac#head](http://www.w3.org/ns/lemon/frac#head)


The **head** property identifies the element of a collocation that its scores are about. A collocation must not have more than one head.

<div class="description">

**domain:** <tt>frac:Collocation</tt>

**range:** <tt>frac:Observable</tt>
</div>
</div>

As an example, the relative frequency score is the number of occurrences of a collocation relative to the overall frequency of its head.
    
<div class="note">
The function of the property `frac:head` is restricted to indicate the directionality of asymmetric collocation scores. It must not be confused with the notion of "head" in certain fields of linguistics, e.g., dependency syntax. 
</div>

<div class="note">
`frac:head` should not be used to model the structure of collocation dictionaries, i.e., the selection of collocations to be displayed with a particular head word. For these functions, please resort to the *lexicog* vocabulary. 
</div>
    
The most elementary level of a collocation is an n-gram, as provided, for example, by [Google Books](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html), which provide n-gram frequencies per publication year as tab-separated values. For 2008, the 2012 edition provides the following statistics for the bigram _kill_ + _switch_.

<aside class="example" title="Example: Google Books Ngram">

```csv
# form-form bigrams
kill    switch  2008    199 121

# form-lexeme bigrams
kill    switch_NOUN 2008    187 115
kill    switch_VERB 2008    8   8

# lexeme-form bigrams
kill_ADJ    switch  2008    70  48
kill_NOUN   switch  2008    89  64
kill_VERB   switch  2008    40  30

# lexeme-lexeme bigrams
kill_VERB   switch_VERB 2008    2   2
kill_NOUN   switch_NOUN 2008    83  61
kill_VERB   switch_NOUN 2008    35  26
kill_ADJ    switch_NOUN 2008    69  48
kill_NOUN   switch_VERB 2008    6   6` </pre>
```

In this example, forms are string values (cf. <tt>ontolex:LexicalForm</tt>), lexemes are string values with parts-of-speech (cf. <tt>ontolex:LexicalEntry</tt>). A partial ontolex-frac representation is given below:

```turtle
# kill (verb)
:kill_v a ontolex:LexicalEntry;
  lexinfo:partOfSpeech lexinfo:verb;
  ontolex:canonicalForm :kill_cf.

# kill (canonical form)
:kill_cf ontolex:writtenRep "kill"@en.

# switch (noun)
:switch_n a ontolex:LexicalEntry;
  lexinfo:partOfSpeech lexinfo:noun;
  ontolex:canonicalForm :switch_cf.

# switch (canonical form)
:switch_cf ontolex:writtenRep "switch"@en.

# form-form bigrams
[ rdf:_1 :kill_cf; rdf:_2 :switch_cf ] a frac:Collocation, rdf:Seq ;
  rdf:value "199";
  dct:description "2-grams, English Version 20120701, word frequency";
  frac;observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.

[ rdf:_1 :kill_cf; rdf:_2 :switch_cf ] a frac:Collocation, rdf:Seq ; 
  rdf:value "121";
  dct:description "2-grams, English Version 20120701, document frequency";
  frac:observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.

# form-lexeme bigrams
[ rdf:_1 :kill_cf; rdf:_2 :switch_n ] a frac:Collocation, rdf:Seq ;
  rdf:value "187";
  dct:description "2-grams, English Version 20120701, word frequency";
  frac:observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.

[ rdf:_1 :kill_cf, rdf:_2 :switch_n ] a frac:Collocation, rdf:Seq ;
  rdf:value "115";
  dct:description "2-grams, English Version 20120701, document frequency";
  frac:observedIn <https://books.google.com/ngrams>;
  dct:temporal "2008"^^xsd:date;
  lexinfo:termType lexinfo:idiom.` </pre>
```

</aside>

The second example illustrates more complex types of collocation are provided as provided by the [Wortschatz](http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012) portal (scores and definitions as provided for [beans](http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012&word=beans), [spill the beans](http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012&word=spill+the+beans), etc.

<aside class="example" title="Example: Wortschatz Collocation">

```turtle
@prefix wsen: <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012&word=>
# selected lexical entries
# (we assume that every Wortschatz word is an independent lexical entry)
wsen:beans a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "beans"@en.
wsen:spill a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "spill"@en.
wsen:green a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "green"@en.
wsen:about a ontolex:LexicalEntry;
  ontolex:canonicalForm/ontolex:writtenRep "about"@en

# collocations, non-lexicalized
[ rdfs:member wsen:spill, wsen:beans ] a frac:Collocation;
  rdf:value "182";
  dct:description "cooccurrences in the same sentence, unordered";
  frac:observedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>.

[ rdf:_1 wsen:green; rdf:_2 wsen:beans ] a frac:Collocation, rdf:Seq ;
  rdf:value "778";
  dct:description "left neighbor cooccurrence";
  frac:observedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>;
  lexinfo:termType lexinfo:idiom.

 [ rdf:_1 wsen:beans; rdf:_2 wsen:about ] a frac:Collocation, rdf:Seq;
  rdf:value "35";
  dct:description "right neighbor cooccurrence";
  frac:observedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>;
  lexinfo:termType lexinfo:idiom.

# multi-word expression, lexicalized (!)
wsen:spill+the+beans a ontolex:MultiWordExpression;
  ontolex:canonicalForm/ontolex:writtenRep "spill the beans"@en.

[ rdfs:member wsen:beans, wsen:spill+the+beans ] a frac:Collocation;
  rdf:value "401";
  dct:description "cooccurrences in the same sentence, unordered";
  frac:obsevedIn <http://corpora.uni-leipzig.de/en/res?corpusId=eng_news_2012>.
```
</aside>

<div class="note">

Again, it is recommended to define resource-specific subclasses of <tt>frac:Collocation</tt> with default values for <tt>dct:description</tt>, <tt>frac:obsevedIn</tt>, and (where applicable) <tt>lexinfo:termType</tt>.

</div>

</section>

<section id="annotation">

## Corpus Annotation (non-normative)

<div class="note">

The Ontolex Module for Frequency, Attestation and Corpus Information does not specify a vocabulary for annotating corpora or other data with lexical information, as this is being provided by the [Web Annotation Vocabulary](https://www.w3.org/TR/annotation-vocab/). The following description is non-normative as Web Annotation is defined in a separate W3C recommendation. The definitions below are reproduced, and refined only insofar as domain and range declarations have been refined to our usecase.

</div>

In Web Annotation terminology, the annotated element is the ‘target’, the content of the annotation is the ‘body’, and the process and provenance of the annotation is expressed by properties of <tt>oa:Annotation</tt>.

<div class="entity">

oa:Annotation (Class)

**URI:** [http://www.w3.org/ns/oa#Annotation](http://www.w3.org/ns/oa#Annotation)

**Required Predicates:** [oa:hasTarget](#hastarget), [rdf:type](#rdf-type), [oa:hasBody](#hasbody)

**Recommended Predicates:** [oa:motivatedBy](#motivatedby), [dcterms:creator](#dcterms-creator), [dcterms:created](#dcterms-created)

**Other Predicates:** [oa:styledBy](#styledby), [dcterms:issued](#dcterms-issued), [as:generator](#as-generator)

</div>

<figure>

![](https://www.w3.org/TR/annotation-vocab/images/examples/annotation.png)

<figcaption>oa:Annotation with properties</figcaption>

</figure>

<div class="entity">


oa:hasBody (Object Property)


**URI:** [http://www.w3.org/ns/oa#hasBody](http://www.w3.org/ns/oa#hasBody)

The object of the relationship is a resource that is a body of the Annotation. In the context of _lemon_, the body is an <tt>ontolex:Element</tt></div>

<div class="description">

**Domain:** oa:Annotation

**Range:** ontolex:Element
</div>
</div>

<figure>

![](https://www.w3.org/TR/annotation-vocab/images/examples/hasBody.png)

<figcaption>oa:hasBody</figcaption>
</figure>

<div class="entity">

oa:hasTarget (Object Property)

**URI:** [http://www.w3.org/ns/oa#hasTarget](http://www.w3.org/ns/oa#hasTarget)

The relationship between an Annotation and its Target.

<div class="description">

**Domain:** oa:Annotation
</div>
</div>

The Web Annotation Vocabulary supports different ways to define targets. This includes:

*   plain URI: The target can be a URI defined within the corpus (e.g., if corpus data is provided as native RDF, or by means of the <tt>@about</tt> attribute in an [HTML/XML+RDFa](https://www.w3.org/TR/rdfa-primer/) document, or by means of <tt>@xml:id</tt> in a [TEI/XML](http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.global.html) document).
*   string URI: String URIs provide the possibility to point directly to a text fragment in a web document, using the URI schemas as provided by [RFC5147](https://tools.ietf.org/html/rfc5147) (text files only) or [NIF](http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core/nif-core.html#introduction) (all text-based formats).
*   [oa:TextPositionSelector](https://www.w3.org/TR/annotation-vocab/#textpositionselector): a range of text defined by the start and end positions of the selection in the stream
*   [oa:DataPositionSelector](https://www.w3.org/TR/annotation-vocab/#datapositionselector): a range of data by recording the start and end positions of the selection in the stream
*   [oa:TextQuoteSelector](https://www.w3.org/TR/annotation-vocab/#textquoteselector): The TextQuoteSelector describes a range of text by copying it. The TextQuoteSelector can include some of the text immediately before (a prefix) and after (a suffix) it to distinguish between multiple copies of the same sequence of characters. If this does suffice for disambiguation, all matching text fragments in the document are being annotated.
*   [oa:XPathSelector](https://www.w3.org/TR/annotation-vocab/#xpathselector): select elements and content within a resource that supports the Document Object Model via a specified XPath value.
*   [oa:RangeSelector](https://www.w3.org/TR/annotation-vocab/#rangeselector): identify the beginning and the end of the selection by using other Selectors.

<div class="note">

<tt>oa:Annotation</tt> explicitly allows _n:m_ relations between <tt>ontolex:Element</tt>s and elements in the annotated elements. It is thus sufficient for every <tt>ontolex:Element</tt> to appear in one <tt>oa:hasBody</tt> statement in order to produce a full annotation of the corpus.

</div>

<div class="note">

As for frequency, embeddings, etc., resource-specific annotation classes can be defined by <tt>owl:Restriction</tt> so that modelling effort and verbosity are reduced. These should follow the same conventions.

</div>

</section>

<section id="usage-guidelines">

## Usage guidelines
back to ([Table of Contents](#table-of-contents))

<section id="resource-specific-classes">

### Resource-specific subclasses of FrAC concepts

As corpus-derived information requires provenance and other metadata, the frac module uses reification (class-based modelling) for concepts such as frequency or embeddings. In a data set, this information will be recurring, and for redundancy reduction, we recommend to provide resource-specific subclasses of frac concepts that provide metadata by means of <tt>owl:Restriction</tt>s that provide the value for the respective properties. This was illustrated above for the relevant frac classes.

As a rule of best practice, we recommend for such cases to provide (a copy of) the OWL definitions of resource-specific classes _in the same graph (and file) as the data_. Within the graph containing the data, the following SPARQL 1.1 query _must_ return the full frac definition of all instances of, say, <tt>:EPSDFrequency</tt> (see examples above):

<aside class="example" title="Example: SPARQL query for resource-specific classes">

```sparql
CONSTRUCT {
    ?data a ?class, ?sourceClass; ?property ?value.
} WHERE {
  ?data a ?sourceClass.                   # e.g., [] a :EPSDFrequency
  ?sourceClass (rdfs:subClassOf|owl:equivalentClass)* ?class.
  FILTER(strstarts(str(?class),'http://www.w3.org/ns/lemon/frac#'))
    # ?class: all superclasses of ?sourceClass which are in the frac namespace
  { # return all value restrictions
      ?class (rdfs:subClassOf|owl:equivalentClass)* ?restriction.
      ?restriction a owl:Restriction.
      ?restriction owl:onProperty ?property.
      ?restriction owl:hasValue ?value.
  } UNION {
    # return all directly expressed values
      ?data ?property ?value.
      FILTER(?property in (frac:observedIn,rdf:value))
      # TODO: update list of properties
  }
}
```

</aside>


This query can be used as a test for _frac_ compliancy, and for property ‘inference’. Note that it does not support <tt>owl:intersection</tt> nor <tt>owl:join</tt>, nor <tt>owl:sameAs</tt>.

<div class="note">

> We use the OWL2/DL vocabulary for modelling restrictions. However, _lemon_ is partially compatible with OWL2/DL only in that several modules use <tt>rdf:List</tt> -- which is a reserved construct in OWL2\. Therefore, the primary means of accessing and manipulation _lemon_ and _ontolex-frac_ data is by means of SPARQL, resp., RDF- (rather than OWL-) technology. In particular, we do not guarantee nor require that OWL2/DL inferences can be used for validating or querying _lemon_ and _ontolex-frac_ data.

</div>

> Note: **TODO** analoguous example for corpus-specific collocations

</section>

<section>

### RDF Serializations and CSV

Usually, numerical information drawn from corpora is distributed and shared as comma-separated values (CSV), e.g., ngram lists or embeddings. Ontolex-frac as an RDF vocabulary is agnostic about its serialization (RDF/TTL, RDF/XML, JSON-LD, etc.), but in particular, it is compliant with CSV and related tabular formats by means of W3C recommendations such as [CSV2RDF](https://www.w3.org/TR/csv2rdf/), [RDB Direct Mapping](https://www.w3.org/TR/rdb-direct-mapping/) and the [RDB to RDF Mapping Language](https://www.w3.org/TR/r2rml/). For corpus-derived lexical-semantic information which is typically distributed in CSV, the best practice is to continue to do so, but to provide a mapping to Ontolex-frac as this provides a vocabulary for their interpretation as Linked Data, and thus establishes an interoperability layer over the raw data without creating additional overhead.

<div class="note">

Ontolex-frac is compliant with CSV formats, but its handling of structured information has an impact on the CSV format. In particular, individual dimensions of embeddings must not use comma as separator in order to be mapped to a single literal. For the example embedding of _frak_ above, the first column (containing the word) should be comma-separated, the following columns (containing the embedding) should be white-space separated.

</div>

</section>

</section>



