# Queries

tested with Apache Jena 4.2.0

    $> arq -query query.sparql -data odzic.ttl

## prefixes

    PREFIX : <http://odzic-stuff.tmp/>
    PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX frac: <http://www.w3.org/ns/lemon/frac#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX lexinfo: <http://www.lexinfo.net/ontology/3.0/lexinfo#>

## retrieve all members in their sequential order, both ordered and unordered

    SELECT DISTINCT ?collocation ?member ?order
    WHERE {
      ?collocation a frac:Collocation; ?prop ?member.
      FILTER(?prop=rdfs:member || regex(str(?prop),".*#_[0-9]+$"))
      # note: with RDFS reasoning enabled, we can just query for rdfs:member
      OPTIONAL {
        ?collocation ?nrel ?member.
        FILTER(regex(str(?nrel),".*#_[0-9]+$"))
        BIND(replace(str(?nrel),".*#_([0-9]+)$","$1") as ?order)
      }
    } ORDER BY ?collocation ?order ?member


    -------------------------------------------------
    | collocation        | member           | order |
    =================================================
    | :analyse-in-depth  | :analyse-verb    | "1"   |
    | :analyse-in-depth  | :in-depth-adv    | "2"   |
    | :analyse-in-detail | :analyse-verb    | "1"   |
    | :analyse-in-detail | :in-detail-adv   | "2"   |
    | :analyze-carefully | :analyse-verb    | "1"   |
    | :analyze-carefully | :carefully-adv   | "2"   |
    | :apply-equally     | :apply-v-sense1  | "1"   |
    | :apply-equally     | :equally-adv     | "2"   |
    | :apply-to          | :apply-v-sense1  | "1"   |
    | :apply-to          | :to-prep         | "2"   |
    | :the-same-applies  | :the             | "1"   |
    | :the-same-applies  | :same            | "2"   |
    | :the-same-applies  | :apply-v-applies | "3"   |
    | :the-same-applies  | :apply-v-sense1  | "3"   |
    -------------------------------------------------

## all collocations for a given lexical entry

    # retrieve string representation of all members
    SELECT DISTINCT ?canonicalForm ?pos ?collocation ?isHead
    WHERE {
      ?collocation a frac:Collocation.
      ?collocation ?prop ?observable.
      FILTER(?prop=rdfs:member  || regex(str(?prop),".*#_[0-9]+$"))
      ?entry (ontolex:sense|ontolex:lexicalForm)? ?observable.
      ?entry ontolex:canonicalForm/ontolex:writtenRep ?canonicalForm.
      OPTIONAL {
        ?collocation frac:head ?observable.
        BIND("true" as ?isHead)
      }
      OPTIONAL {
        ?entry lexinfo:partOfSpeech ?pos
      }
    } ORDER BY ?canonicalForm ?pos ?collocation ?isHead

    --------------------------------------------------------------------
    | canonicalForm | pos                 | collocation       | isHead |
    ====================================================================
    | "apply"       |                     | :apply-equally    | "true" |
    | "apply"       |                     | :apply-to         | "true" |
    | "apply"       |                     | :the-same-applies |        |
    | "apply"       |                     | :the-same-applies | "true" |
    | "equally"     | lexinfo:adverb      | :apply-equally    |        |
    | "same"        |                     | :the-same-applies |        |
    | "the"         |                     | :the-same-applies |        |
    | "to"          | lexinfo:preposition | :apply-to         |        |
    --------------------------------------------------------------------

Note that *apply* occurs multiple times if both form and sense are specified.
Also note that we forgot the pos in the head words ;)

## generation: retrieve string representation of all members

    SELECT DISTINCT ?collocation ?string
    WHERE {
      { SELECT ?collocation (GROUP_CONCAT(?wrep; separator=" ") as ?string)
        WHERE {
          { SELECT distinct ?collocation ?member ?wrep ?order
            WHERE {
              ?collocation a frac:Collocation; ?prop ?member.
              FILTER(?prop=rdfs:member || regex(str(?prop),".*#_[0-9]+$"))
              ?member ((^ontolex:sense)?/ontolex:canonicalForm)?/ontolex:writtenRep ?wrep.
              OPTIONAL {
                ?collocation ?nrel ?member.
                FILTER(regex(str(?nrel),".*#_[0-9]+$"))
                BIND(replace(str(?nrel),".*#_([0-9]+)$","$1") as ?order)
              }
            } GROUP BY ?collocation ?member ?wrep ?order
              ORDER BY ?collocation ?order ?member
          }
        } GROUP BY ?collocation
      }
    }


    ------------------------------------------------
    | collocation       | string                   |
    ================================================
    | :apply-equally    | "apply equally"          |
    | :the-same-applies | "the same applies apply" |
    | :apply-to         | "apply to"               |
    ------------------------------------------------

Note that there are two filler elements for position 3 in `:the-same-applies`, hence both the canonical form and the contextualized form
