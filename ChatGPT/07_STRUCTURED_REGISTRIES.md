# Structured Registries

This file preserves the structured CSV layers that support the narrative canon. Each source includes a column list, a short preview, and the full CSV payload.

## Included Sources

- `data_people.csv`
- `data_places.csv`
- `data_relationships.csv`
- `data_chat_memberships.csv`
- `data_aliases.csv`
- `data_business_deals.csv`

---

## Source: `data_people.csv` {#data-people-csv}

### Columns

| Column |
|---|
| `id` |
| `display_name` |
| `full_name` |
| `status` |
| `role_tags` |
| `primary_circle` |
| `first_appearance` |
| `alive_in_story` |
| `age_in_2026` |
| `notes` |

### Preview

| id | display_name | full_name | status | role_tags | primary_circle | first_appearance | alive_in_story | age_in_2026 | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alex_wilson | Alex | Alexander David Wilson | fictional_core | pianist;juilliard_graduate;protagonist | inner_circle |  | true | 22 | Born June 22 2003; Juilliard BM Piano Performance 2025, degree focused on contemporary, classical and jazz; junior-year RAM exchange 2023-24 continued the cross-genre focus; also plays violin and guitar at advanced level from childhood training; no occupation at story-open — one week after graduation, in grace period; no commercial career yet |
| rosie_walker | Rosie | Rosie Walker Wilson | fictional_core | musician;songwriter;matriarch;label_owner | inner_circle |  | true | 80 | Greatest musical artist alive; 34 Grammys; retired 1980; Alex's legal mother |
| homer_wilson | Homer | Sir Homer Wilson KBE | fictional_core | producer;engineer;mentor | inner_circle |  | true | 81 | Greatest record producer/engineer alive; 15 Grammys; knighted 1998; Alex's legal father |
| eleanor_vance | Eleanor | Eleanor Margaret Vance | fictional_core | ceo;business_executive;advisor | inner_circle |  | true | 52 | CEO Walker Holdings ~$18-20B; raised as family niece; Harvard MBA; ex-Goldman |
| tommy_crawford | Tommy | Thomas James Crawford | fictional_core | contractor;best_friend | inner_circle |  | true | 21 | Alex's best friend since kindergarten; Sayre School K-12; Crawford Construction; Woodford County |
| david_wilson | David | David James Wilson | fictional_supporting | musician;deceased | family |  | false |  | Rosie's biological son; Alex's biological father; died overdose 2008 when Alex was 5 |
| sarah_dawson | Sarah | Lady Sarah Anne Dawson Wilson | fictional_supporting | aristocrat;deceased | family |  | false |  | Alex's biological mother; 3rd child of Earl of Fletching; died in childbirth 2003 |
| maria_santos | Maria | Maria Santos | fictional_supporting | chef | nashville_backbone |  | true | 45 | Compound chef; French Laundry/Per Se/CIA trained; known Alex since childhood |

### Full CSV

```csv
id,display_name,full_name,status,role_tags,primary_circle,first_appearance,alive_in_story,age_in_2026,notes
alex_wilson,Alex,Alexander David Wilson,fictional_core,"pianist;juilliard_graduate;protagonist",inner_circle,,true,22,"Born June 22 2003; Juilliard BM Piano Performance 2025, degree focused on contemporary, classical and jazz; junior-year RAM exchange 2023-24 continued the cross-genre focus; also plays violin and guitar at advanced level from childhood training; no occupation at story-open — one week after graduation, in grace period; no commercial career yet"
rosie_walker,Rosie,Rosie Walker Wilson,fictional_core,musician;songwriter;matriarch;label_owner,inner_circle,,true,80,Greatest musical artist alive; 34 Grammys; retired 1980; Alex's legal mother
homer_wilson,Homer,Sir Homer Wilson KBE,fictional_core,producer;engineer;mentor,inner_circle,,true,81,Greatest record producer/engineer alive; 15 Grammys; knighted 1998; Alex's legal father
eleanor_vance,Eleanor,Eleanor Margaret Vance,fictional_core,ceo;business_executive;advisor,inner_circle,,true,52,CEO Walker Holdings ~$18-20B; raised as family niece; Harvard MBA; ex-Goldman
tommy_crawford,Tommy,Thomas James Crawford,fictional_core,contractor;best_friend,inner_circle,,true,21,Alex's best friend since kindergarten; Sayre School K-12; Crawford Construction; Woodford County
david_wilson,David,David James Wilson,fictional_supporting,musician;deceased,family,,false,,"Rosie's biological son; Alex's biological father; died overdose 2008 when Alex was 5"
sarah_dawson,Sarah,Lady Sarah Anne Dawson Wilson,fictional_supporting,aristocrat;deceased,family,,false,,"Alex's biological mother; 3rd child of Earl of Fletching; died in childbirth 2003"
maria_santos,Maria,Maria Santos,fictional_supporting,chef,nashville_backbone,,true,45,Compound chef; French Laundry/Per Se/CIA trained; known Alex since childhood
dale_shackleford,Dale,Dale Shackleford,fictional_supporting,estate_manager,nashville_backbone,,true,58,Compound estate manager; Woodford County family; lives on property
loretta_mae,Loretta,Loretta Mae,fictional_supporting,household_manager;personal_assistant,nashville_backbone,,true,62,Compound household manager and Rosie/Homer PA since 1990s
kevin_marsh,Kevin,Kevin Marsh,fictional_supporting,close_protection_officer;security,inner_circle,,true,34,Alex's CPO; ex-USSS Presidential Protective Division; 2 years with Alex
nadia_hassani,Nadia,Nadia Hassani,fictional_supporting,executive_assistant;operations,inner_circle,,true,28,Alex's EA; London-based; hired from Quintessentially; manages all logistics
sophie_kalu,Sophie,Sophie Kalu,fictional_supporting,personal_assistant,inner_circle,,true,25,Alex's PA; Nigerian-British; hired early 2025 under Nadia
james_latham,James,James Latham,fictional_supporting,management;diplomat;al_x_head,industry,,true,48,Head of AL.X management division; British; ex-FCDO diplomat; Scooter Braun blacklist enforcer
priya_chandra,Priya,Priya Chandra,fictional_supporting,management;al_x_coordinator,industry,,true,32,AL.X senior coordinator; reports to Latham
oliver_wren,Oliver,Oliver Wren,fictional_supporting,management;al_x_analyst,industry,,true,26,AL.X analyst; youngest on the team
graham_forsyth,Graham,Graham Forsyth,fictional_supporting,cfo;finance,industry,,true,54,Walker Holdings CFO; Deloitte background; Eleanor's right hand
diane_prescott,Diane,Diane Prescott,fictional_supporting,general_counsel;lawyer,industry,,true,47,Walker Holdings General Counsel; entertainment law; estate planning
peter_aldridge,Peter,Peter Aldridge,fictional_supporting,investment_manager;finance,industry,,true,39,Walker Holdings investments director; Bridgewater background
cody_ashford,Cody,Cody Ashford,fictional_supporting,sayre_boy;friend,inner_circle,,true,22,Sayre Boys core; all-caps energy; catalytic personality; Woodford County
jake_patterson,Jake,Jake Patterson,fictional_supporting,sayre_boy;friend,inner_circle,,true,22,Sayre Boys core; minimal communication style; horse/land expertise; logistics-first
danny_harlan,Danny,Danny Harlan,fictional_supporting,sayre_boy;friend,inner_circle,,true,22,Sayre Boys core; dry understated irony; arrives late with the perfect line
jim_crawford,Jim,Jim Crawford,fictional_supporting,contractor;businessman;family_friend,family,,true,52,Tommy's father; owns Crawford Construction (~400 employees); father figure to Alex
darlene_crawford,Darlene,Darlene Crawford,fictional_supporting,teacher;family_friend,family,,true,50,Tommy's mother; school teacher 25 years; fed Alex approximately 10000 meals
kayla_crawford,Kayla,Kayla Crawford,fictional_supporting,student;family_friend,family,,true,19,Tommy's younger sister; long-running crush on Alex (mutual joke)
richard_dawson,The Earl,Richard Dawson 7th Earl of Fletching,real,aristocrat;businessman,family,,true,79,"Alex's maternal grandfather; Eton/Oxford; City finance background; Fletching Park East Sussex; half-Italian-royal by birth — mother was HRH Princess Isabella of Savoy-Aosta (1918-2005); succeeded to earldom on father's death in 1988; fluent Italian through his mother"
margaret_dawson,The Countess,Margaret Whitelock Dawson Countess of Fletching,real,aristocrat,family,,true,77,"Alex's maternal grandmother; born 1949 as Margaret Whitelock; Cheltenham Ladies' College; holds family emotional architecture; half-Greek-royal by birth — mother was HRH Princess Anastasia of Greece and Denmark (1924-2001); father was General Sir Edward Whitelock; married Richard Dawson 1971; became Countess of Fletching on his accession 1988; fluent Greek and French through her mother"
james_dawson,James,James Dawson Viscount Hartfield,real,aristocrat;private_equity,family,,true,56,Eldest Dawson child; heir to earldom; Hartfield Capital London; Jonathan's father
jonathan_dawson,Jonathan,The Honourable Jonathan Dawson,real,aristocrat;student;london_lot,london_lot,,true,23,Alex's cousin; Westminster School then Oxford (PPE); works at father's firm; Dawson Cousins chat initiator
lucas_ashby,Lucas,Lucas Ashby,real,student;architect;london_lot,london_lot,,true,22,Alex's cousin; Caroline's son; Bartlett/UCL architecture; Notting Hill; warmest Dawson connection
beatrice_dawson,Beatrice,Beatrice Dawson,real,student;aristocrat,family,,true,20,Jonathan's sister; Edinburgh counterpoint; sardonic/direct
lady_caroline_ashby,Caroline,Lady Caroline Ashby née Dawson,real,aristocrat,family,,true,47,Sarah's closest sibling; married Henry Ashby; Lucas's mother; quietly reparative with Alex
henry_ashby,Henry,Henry Ashby,real,banker;private_equity,family,,true,50,Caroline's husband; banker then private equity; Lucas's father
elton_john,Elton,Sir Elton John CBE,real,musician;godparent;circle_member,inner_circle,,true,78,Alex's godfather; Rosie/Homer decades-long friend; Phoenix Hollow Circle; Zachary & Elijah's father
chris_martin,Chris,Chris Martin,real,musician;godparent;circle_member,inner_circle,,true,48,Alex's godfather; Apple & Moses's father; low-drama practical presence; Phoenix Hollow Circle
donatella_versace,Donatella,Donatella Versace,real,fashion_designer;godparent;circle_member,inner_circle,,true,70,Alex's godmother; Versace house; high-conviction aesthetic authority; calls Alex "Alexander"
stella_mccartney,Stella,Stella McCartney,real,fashion_designer;godparent;circle_member,inner_circle,,true,54,Alex's godmother; McCartney lineage; values-forward fashion; London-based style advisor
apple_martin,Apple,Apple Blythe Alison Martin,real,legacy_kid;friend,summer_house,,true,21,Alex's god-sister; sibling-close; NOT romantic; born May 14 2004; Chris Martin/Gwyneth Paltrow's daughter
moses_martin,Moses,Moses Bruce Anthony Martin,real,legacy_kid,family,,true,19,Chris Martin/Gwyneth Paltrow's son; Alex's god-sibling; born April 8 2006
zachary_furnish_john,Zachary,Zachary Jackson Levon Furnish-John,real,legacy_kid,family,,true,15,Elton's son; Alex's god-sibling; born Dec 25 2010
elijah_furnish_john,Elijah,Elijah Joseph Daniel Furnish-John,real,legacy_kid,family,,true,14,Elton's son; Alex's god-sibling; born Jan 11 2013
beyonce,Beyoncé,Beyoncé Giselle Knowles-Carter,real,musician;circle_member,phoenix_hollow,,true,44,Phoenix Hollow Inner Circle; strategy + craft authority; sparse weighted presence
adele,Adele,Adele Laurie Blue Adkins,real,musician;circle_member,phoenix_hollow,,true,37,Phoenix Hollow Inner Circle; blunt warmth; wrote half of 25 at compound
lady_gaga,Gaga,Lady Gaga,real,musician;actress;circle_member,phoenix_hollow,,true,39,Phoenix Hollow Inner Circle; conceptual but concrete; story-first framework language
taylor_swift,Taylor,Taylor Swift,real,musician;circle_member,phoenix_hollow,,true,36,Phoenix Hollow Inner Circle; 2019 masters conversation with Rosie; ghost/lurker in Summer House chat
stevie_nicks,Stevie,Stevie Nicks,real,musician;circle_member;mentor,phoenix_hollow,,true,77,Phoenix Hollow Inner Circle; de facto aunt/godmother; image-rich reflective presence; annual compound residency
dolly_parton,Dolly,Dolly Rebecca Parton,real,musician;songwriter;circle_member,phoenix_hollow,,true,80,Phoenix Hollow Inner Circle; de facto aunt; warmth + blunt practical counsel; Nashville anchor
paul_mccartney,Paul,Sir Paul McCartney,real,musician;circle_member,phoenix_hollow,,true,83,Phoenix Hollow Inner Circle; long-view musical benchmark; quiet validator; Stella's father
joni_mitchell,Joni,Joni Mitchell,real,musician;songwriter;circle_member,phoenix_hollow,,true,82,Phoenix Hollow Inner Circle; high-rigor artistic truth voice; Rosie's peer
brandi_carlile,Brandi,Brandi Carlile,real,musician;mentor;circle_member,phoenix_hollow,,true,44,Phoenix Hollow Inner Circle; contemporary bridge generation; annual compound residency; like older sister to Alex
david_gilmour,David G,David Gilmour,real,musician;producer;circle_member,phoenix_hollow,,true,79,Homer's closest friend; Pink Floyd; craft-first minimal talker; periodic compound/studio engagement
bruce_springsteen,Bruce,Bruce Springsteen,real,musician;circle_member,phoenix_hollow,,true,76,Phoenix Hollow World Stage; compound presence; The Boss
bono,Bono,Paul David Hewson,real,musician;activist;circle_member,phoenix_hollow,,true,65,Phoenix Hollow World Stage; U2; compound visitor
the_edge,The Edge,David Howell Evans,real,musician;circle_member,phoenix_hollow,,true,64,Phoenix Hollow World Stage; U2; compound visitor
dave_grohl,Dave,Dave Grohl,real,musician;circle_member,phoenix_hollow,,true,56,Phoenix Hollow World Stage; Foo Fighters/Nirvana; compound visitor
jack_white,Jack,Jack White,real,musician;producer;circle_member,phoenix_hollow,,true,50,Phoenix Hollow World Stage; White Stripes; compound residency visits
alicia_keys,Alicia,Alicia Keys,real,musician;circle_member,phoenix_hollow,,true,44,Phoenix Hollow World Stage; compound writing/recording visits; Homer-produced album
billie_eilish,Billie,Billie Eilish Pirate Baird O'Connell,real,musician;circle_member,phoenix_hollow,,true,24,Phoenix Hollow World Stage; compound visits; contemporary generation crossover
harry_styles,Harry,Harry Edward Styles,real,musician;model;circle_member,phoenix_hollow,,true,31,Phoenix Hollow World Stage and Summer House; British fashion/music crossover
dua_lipa,Dua,Dua Lipa,real,musician;circle_member,phoenix_hollow,,true,30,Phoenix Hollow World Stage and Summer House; British pop anchor
lana_del_rey,Lana,Elizabeth Woolridge Grant,real,musician;circle_member,phoenix_hollow,,true,40,Phoenix Hollow World Stage; melancholic art pop; compound presence
meryl_streep,Meryl,Mary Louise Streep,real,actress;circle_member,phoenix_hollow,,true,76,Phoenix Hollow World Stage; Hollywood royalty; compound visitor
cate_blanchett,Cate,Catherine Élise Blanchett,real,actress;circle_member,phoenix_hollow,,true,56,Phoenix Hollow World Stage; Australian acting royalty; compound visitor
tom_hanks,Tom,Thomas Jeffrey Hanks,real,actor;circle_member,phoenix_hollow,,true,69,Phoenix Hollow World Stage; compound visitor
george_clooney,George,George Timothy Clooney,real,actor;filmmaker;circle_member,phoenix_hollow,,true,64,Phoenix Hollow World Stage; compound visitor
amal_clooney,Amal,Amal Ramzi Clooney,real,lawyer;activist;circle_member,phoenix_hollow,,true,47,Phoenix Hollow World Stage; George's wife; compound visitor
florence_pugh,Florence,Florence Pugh,real,actress;circle_member,phoenix_hollow,,true,30,Phoenix Hollow World Stage and Summer House; British actress; active London social circle
anya_taylor_joy,Anya,Anya Taylor-Joy,real,actress;circle_member,phoenix_hollow,,true,29,Phoenix Hollow World Stage and Summer House; British-Argentine actress
sofia_coppola,Sofia,Sofia Carmina Coppola,real,filmmaker;circle_member,phoenix_hollow,,true,52,Phoenix Hollow World Stage; filmmaker; compound visitor
greta_gerwig,Greta,Greta Celeste Gerwig,real,filmmaker;circle_member,phoenix_hollow,,true,42,Phoenix Hollow World Stage; filmmaker; compound visitor
wes_anderson,Wes,Wesley Wales Anderson,real,filmmaker;circle_member,phoenix_hollow,,true,56,Phoenix Hollow World Stage; filmmaker; compound visitor
martin_scorsese,Marty,Martin Charles Scorsese,real,filmmaker;circle_member,phoenix_hollow,,true,83,Phoenix Hollow World Stage; filmmaker; compound visitor
steven_spielberg,Steven,Steven Allan Spielberg,real,filmmaker;circle_member,phoenix_hollow,,true,78,Phoenix Hollow World Stage; filmmaker; compound visitor
annie_leibovitz,Annie,Anna-Lou Leibovitz,real,photographer;circle_member,phoenix_hollow,,true,75,Phoenix Hollow Fashion/Visual; Vogue photographer; shot Alex's debut Vogue cover Sept 2025
edward_enninful,Edward,Edward Enninful,real,fashion_editor;circle_member,phoenix_hollow,,true,52,Phoenix Hollow Fashion/Visual; former British Vogue EIC; fashion connections
alessandro_michele,Alessandro,Alessandro Michele,real,fashion_designer;circle_member,phoenix_hollow,,true,52,Phoenix Hollow Fashion/Visual; former Gucci creative director; compound visitor
barack_obama,Barack,Barack Hussein Obama II,real,politician;circle_member,phoenix_hollow,,true,64,Phoenix Hollow Public Figures; White House letter in Homer's library; low-frequency high-impact chat presence
michelle_obama,Michelle,Michelle LaVaughn Obama,real,activist;author;circle_member,phoenix_hollow,,true,61,Phoenix Hollow Public Figures; compound visitor alongside Barack
lenny_kravitz,Lenny,Leonard Albert Kravitz,real,musician;circle_member,phoenix_hollow,,true,61,Phoenix Hollow Public Figures; Rosie connection; Apple Martin's godfather
gwyneth_paltrow,Gwyneth,Gwyneth Kate Paltrow,real,actress;entrepreneur;circle_member,phoenix_hollow,,true,53,Phoenix Hollow Public Figures; Apple's mother; Chris Martin ex; compound visitor
lila_moss,Lila,Lila Moss Hack,real,model;legacy_kid,summer_house,,true,23,Kate Moss's daughter; Phoenix Hollow Legacy Core and Summer House; fashion world; Sardinia regular
rocco_ritchie,Rocco,Rocco Ritchie,real,artist;legacy_kid,summer_house,,true,25,Madonna/Guy Ritchie's son; Phoenix Hollow Legacy Core; has own summer circuit
iris_law,Iris,Iris Law,real,model;photographer;legacy_kid,summer_house,,true,24,Jude Law's daughter; Phoenix Hollow Legacy Core; creative/art world; summer circuit
lady_amelia_windsor,Amelia,Lady Amelia Windsor,real,young_royal;model,summer_house,,true,30,Duke of Kent's granddaughter; Phoenix Hollow Legacy Core and Summer House; aristocratic fashion
samuel_chatto,Samuel,Samuel Chatto,real,young_royal;artist,summer_house,,true,28,Princess Margaret's grandson; Phoenix Hollow Legacy Core and Summer House; low-key artist
arthur_chatto,Arthur,Arthur Chatto,real,young_royal,summer_house,,true,26,Princess Margaret's grandson; Phoenix Hollow Legacy Core and Summer House
chad_smith,Chad,Chad Smith,real,musician;drummer;nashville_backbone,nashville_backbone,,true,63,Red Hot Chili Peppers drummer; Phoenix Hollow Nashville Backbone; compound session work
steve_jordan,Steve,Steve Jordan,real,musician;drummer;nashville_backbone,nashville_backbone,,true,69,Session drummer; Phoenix Hollow Nashville Backbone; Rolling Stones touring drummer
pino_palladino,Pino,Pino Palladino,real,musician;bassist;nashville_backbone,nashville_backbone,,true,65,Session bassist; Phoenix Hollow Nashville Backbone; compound session work
paul_franklin,Paul,Paul Franklin,real,musician;steel_guitar;nashville_backbone,nashville_backbone,,true,68,Session steel guitar; Phoenix Hollow Nashville Backbone; Nashville institution
freddie_ashworth,Freddie,Frederick James Ashworth,fictional_supporting,aristocrat;friend;london_lot,london_lot,,true,22,London Lot execution engine; Westminster School peer; suggests plan and converts vague interest to attendance
jess_okonkwo,Jess,Jessica Okonkwo,fictional_supporting,musician;friend;london_lot,london_lot,,true,22,London Lot music discovery voice; RAM-adjacent curation; Wigmore-adjacent taste
cosima_hicks,Cosima,Cosima Hicks,fictional_supporting,artist;sculptor;friend;london_lot,london_lot,,true,23,Sculptor; created Sound & Bone piece for Alex; art/culture selector; dry tone; made cyanotype/piano-wire sculpture for Alex
hugo_manners,Hugo,Hugo Manners,fictional_supporting,aristocrat;friend;london_lot,london_lot,,true,23,London Lot country/polo lane activator; Guards Polo Club world; cricket/sport focus
raye,Raye,Rachel Agatha Keen,real,musician;london_lot,london_lot,,true,27,South London R&B/pop; London Lot and Summer House; part of British music scene
stormzy,Stormzy,Michael Ebenazer Kwadjo Omari Jr Owuo,real,musician;london_lot,london_lot,,true,31,Grime pioneer; London Lot and Summer House; British Power Anchor
central_cee,Central Cee,Oakley Caesar-Su,real,musician;london_lot,london_lot,,true,26,UK rap; London Lot and Summer House; British Power Anchor
tom_holland,Tom,Thomas Stanley Holland,real,actor;london_lot,london_lot,,true,29,Spider-Man actor; London Lot and Summer House; British Power Anchor
paul_mescal,Paul M,Paul Mescal,real,actor;london_lot,summer_house,,true,30,Irish actor; Summer House British Power Anchor; London social world overlap
maya_hawke,Maya,Maya Ray Thurman-Hawke,real,actress;musician;legacy_kid,summer_house,,true,27,Uma Thurman/Ethan Hawke's daughter; Summer House Legacy; Hudson Valley LA crossover
barry_keoghan,Barry,Barry Keoghan,real,actor;london_lot,summer_house,,true,32,Irish actor; Summer House NY/London extras; Dublin-London-LA crossover
lennon_gallagher,Lennon,Lennon Francis Gallagher,real,model;legacy_kid,summer_house,,true,25,Liam Gallagher's son; Summer House Legacy; fashion and music world
anais_gallagher,Anaïs,Anaïs Gallagher,real,model;legacy_kid,summer_house,,true,24,Noel Gallagher's daughter; Summer House Legacy; fashion world
damian_hurley,Damian,Damian Charles Hurley,real,model;actor;legacy_kid,summer_house,,true,23,Elizabeth Hurley's son; Summer House Legacy; British model/actor
nora_yoon,Nora,Nora Yoon,fictional_supporting,musician;pianist;friend;juilliard,ny_lot,,true,22,Juilliard peer; real friend; "that passage is wrong"; Korean-American; direct musical honesty
marcus_delacroix,Marcus,Marcus Delacroix,fictional_supporting,musician;bassist;friend;juilliard,ny_lot,,true,23,Juilliard peer; NYC nightlife launch energy; all-caps summons; "9PM. NOT OPTIONAL."
derrick_washington,Derrick,Derrick Washington,fictional_supporting,musician;producer;friend;juilliard,ny_lot,,true,24,Juilliard peer; late-night studio specialist; appears after 10pm; "studio. midnight."
sasha_volkov,Sasha,Alexander Volkov,fictional_supporting,musician;violinist;friend;juilliard,ny_lot,,true,22,Juilliard peer; Russian-American violinist; concise one-word interest signals
jin_park,Jin,Jin-Ho Park,fictional_supporting,musician;cellist;friend;juilliard,ny_lot,,true,23,Juilliard peer; Korean-American cellist; terse progress updates
henry_cabot,Henry,Henry Cabot,fictional_supporting,socialite;friend;ny_lot,ny_lot,,true,24,NYC social scene; table access and venue leverage; connects Juilliard to downtown
sam_okafor,Sam,Samuel Okafor,fictional_supporting,musician;friend;ny_lot,ny_lot,,true,23,Bridge node between Juilliard and NYC club ecosystem; Nigerian-American
dr_catherine_marlowe,Dr. Marlowe,Dr. Catherine Marlowe,fictional_supporting,professor;piano_faculty;juilliard,industry,,true,52,Juilliard piano faculty; Alex's primary professor; "Best undergraduate recital in twenty years"; "Again."
dr_amara_osei,Dr. Osei,Dr. Amara Osei,fictional_supporting,professor;voice_faculty;juilliard,industry,,true,48,Juilliard voice faculty; "support the breath"; pushing Alex toward voice training
dr_james_whitfield,Dr. Whitfield,Dr. James Whitfield,fictional_supporting,professor;composition_faculty;juilliard,industry,,true,55,Juilliard composition/theory faculty; "structurally this turns too soon"
timothee_chalamet,Timothée,Timothée Hal Chalamet,real,actor;musician,ny_lot,,true,30,French-American actor; NY Lot and Summer House; Juilliard-adjacent; actually plays piano
zoe_kravitz,Zoë,Zoë Isabella Kravitz,real,actress;model;legacy_kid,ny_lot,,true,36,Lenny Kravitz's daughter; NY Lot; Zero Bond crowd; Legacy Admissions
bella_hadid,Bella,Isabella Khair Hadid,real,model;legacy_kid,ny_lot,,true,29,Model; NY Lot; fashion world crossover; Legacy Admissions adjacent
gigi_hadid,Gigi,Jelena Noura Hadid,real,model;legacy_kid,ny_lot,,true,30,Model; NY Lot; fashion world crossover; Legacy Admissions adjacent
kaia_gerber,Kaia,Kaia Jordan Gerber,real,model;actress;legacy_kid,ny_lot,,true,24,Cindy Crawford's daughter; LA Lot and Summer House; Legacy Admissions; friendly with Alex
jacob_elordi,Jacob,Jacob Elordi,real,actor,summer_house,,true,28,Australian actor; Summer House core voice; minimal post maximal effect
emma_chamberlain,Emma,Emma Frances Chamberlain,real,content_creator;entrepreneur,summer_house,,true,23,Content creator; Summer House high-volume chaos accelerator; spiral posting style
jenna_ortega,Jenna,Jenna Marie Ortega,real,actress,summer_house,,true,23,Actress; Summer House low-frequency impact; single-line dry hits; rare commitments
sabrina_carpenter,Sabrina,Sabrina Annlynn Carpenter,real,musician;actress,summer_house,,true,26,Pop musician; Summer House sharp thread closer; fast last-word tendency
zendaya,Zendaya,Zendaya Maree Stoermer Coleman,real,actress;musician,summer_house,,true,29,Summer House ghost/lurker; high-signal low-frequency
olivia_rodrigo,Olivia,Olivia Isabel Rodrigo,real,musician,summer_house,,true,22,Summer House seasonal tourist; pop songwriter
ice_spice,Ice Spice,Isis Gaston,real,musician,summer_house,,true,22,Bronx rapper; Summer House seasonal tourist
jack_schlossberg,Jack,Jack Schlossberg,real,kennedy_family;lawyer,summer_house,,true,33,JFK's grandson; Summer House seasonal tourist; Legacy Admissions
jeremy_allen_white,Jeremy,Jeremy Allen White,real,actor,summer_house,,true,33,Actor; Summer House seasonal tourist; London/NYC crossover
austin_butler,Austin,Austin Robert Butler,real,actor,summer_house,,true,33,Actor; Summer House seasonal tourist
naomi_campbell,Naomi,Naomi Elaine Campbell,real,model;activist,summer_house,,true,55,Supermodel; Summer House fashion week bridge; Glastonbury presence
vittoria_ceretti,Vittoria,Vittoria Ceretti,real,model,satellite,,true,27,Italian supermodel; confirmed hookup July/Aug 2025 Sardinia; Daily Mail confirmation
taylor_russell,Taylor R,Taylor Russell,real,actress,satellite,,true,29,Canadian actress; one_photo hookup evidence Carnegie Hall Oct 2025; Page Six
hunter_schafer,Hunter,Hunter Schafer,real,model;actress,satellite,,true,25,Model/actress; strongly suspected hookup Paris FW Sept 2025; DeuxMoi sourced
addison_rae,Addison,Addison Rae Easterling,real,content_creator;actress,satellite,,true,24,Content creator/actress; strongly suspected hookup NYC-Paris FW Sept 2025; DeuxMoi sourced
alix_earle,Alix,Alix Earle,real,content_creator,satellite,,true,24,Content creator; rumored hookup Ibiza July 2025; DeuxMoi sourced
dove_cameron,Dove,Dove Olivia Cameron,real,actress;musician,satellite,,true,29,Actress/musician; rumored hookup London June 2025; DeuxMoi sourced
tommaso_corsini,Tommaso,Tommaso Corsini,fictional_supporting,architect;socialite;friend,la_terrazza,,true,26,La Terrazza anchor; Milan/Sardinia; knows Porto Cervo since childhood; calm planner
edo_ferretti,Edo,Edoardo Ferretti,fictional_supporting,dj;promoter;friend,la_terrazza,,true,27,Chaos anchor; DJ/promoter; Rome/Ibiza/everywhere; Sardinia party catalyst
camille_aubert,Camille,Camille Aubert,fictional_supporting,gallerist;friend,la_terrazza,,true,25,Parisian gallerist; art world anchor; connects Alex to contemporary art circuit
lucia_montero,Lucía,Lucía Montero,fictional_supporting,student;friend,la_terrazza,,true,24,Madrid/London; sharp and political; brings critical perspective to summer circuit
felix_arnoult,Félix,Félix Arnoult,fictional_supporting,wine_heir;friend,la_terrazza,,true,28,French wine family; brings wine to everything; Paris/NYC crossover
giulia_agnelli,Giulia,Giulia Agnelli,fictional_supporting,socialite;fashion;friend,la_terrazza,,true,26,Milan/Italian old money; fashion world; drops in and out; Tommaso-connected
prince_achille_bourbon,Achille,Prince Achille of Bourbon-Two Sicilies,real,royalty;finance,la_terrazza,,true,26,Italian royal house; Sardinia/Capri/Amalfi summer circuit; Tommaso-connected
olympia_of_greece,Olympia,Princess Olympia of Greece,real,royalty;model,summer_house,,true,29,Greek royal; London/New York; bridges London Lot and La Terrazza; fashion world
pierre_casiraghi,Pierre,Pierre Casiraghi,real,royalty,la_terrazza,,true,37,Grace Kelly's grandson; Monaco; sailing; overlaps Mediterranean summer circuit
countess_cosima_von_bulow,Cosima V,Countess Cosima von Bülow,fictional_supporting,aristocrat;art_world,la_terrazza,,true,27,Austrian-Italian; Vienna/Milan; art/fashion circuit; connects Central European dimension
rick_rubin,Rick,Frederick Jay Rubin,real,producer;executive,industry,,true,61,Legendary producer; visits Homer annually; compound connection
brian_eno,Brian,Brian Peter George St John le Baptiste de la Salle Eno,real,producer;musician,industry,,true,77,Producer/ambient pioneer; corresponds with Homer on sound theory; letters relationship
daniel_lanois,Daniel,Daniel Lanois,real,producer,industry,,true,73,Producer; ongoing contact with Homer; U2/Dylan records
t_bone_burnett,T Bone,Joseph Henry Burnett,real,producer;musician,industry,,true,76,Producer; ongoing contact with Homer; Nashville/Americana world
irving_azoff,Irving,Irving Azoff,real,manager;executive,industry,,true,76,Industry manager; calling Eleanor about Alex post-graduation; Eagles/Eagles management
princess_maria_olympia,Maria-Olympia,Princess Maria-Olympia of Greece and Denmark,real,royalty;model,summer_house,,true,29,Greek/Danish royal; Summer House Young Royals tier; fashion world
princess_alexia,Alexia,Princess Alexia of the Netherlands,real,royalty,summer_house,,true,19,Dutch royal family; Summer House Young Royals tier
achileas_of_greece,Achileas,Prince Achileas-Andreas of Greece and Denmark,real,royalty,la_terrazza,,true,24,Greek/Danish royal; Summer House Young Royals; Mediterranean circuit; Greco-British royal ties
kate_moss,Kate,Katherine Ann Moss,real,model;circle_member,phoenix_hollow,,true,51,Supermodel; Lila's mother; Phoenix Hollow legacy parent tier
madonna,Madonna,Madonna Louise Ciccone,real,musician;circle_member,phoenix_hollow,,true,67,Pop icon; Phoenix Hollow legacy parent tier; Rocco's mother
jude_law,Jude,David Jude Heyworth Law,real,actor;circle_member,phoenix_hollow,,true,52,Actor; Phoenix Hollow legacy parent tier; Iris's father
tyrone_lebon,Tyrone,Tyrone Lebon,real,photographer;editorial;fashion_adjacent,summer_house,,true,37,British editorial photographer; Dior Men/Miu Miu/Bottega clients; London and Milan circuit
cass_bird,Cass,Cass Bird,real,photographer;editorial;portrait,summer_house,,true,46,American portrait/editorial photographer; Vogue/GQ/Dior/Saint Laurent clients; NY and European circuit
morgan_maassen,Morgan,Morgan Maassen,real,photographer;surf;lifestyle,summer_house,,true,32,Surf and lifestyle photographer/filmmaker; Vogue crossover; seasonal Ibiza/Sardinia presence
campbell_addy,Campbell,Campbell Addy,real,photographer;editorial;filmmaker,summer_house,,true,31,British-Ghanaian photographer and filmmaker; Valentino/Bottega/Burberry clients; London crossover
ibrahim_kamara,Ibrahim,Ibrahim Kamara,real,creative_director;editorial;fashion,summer_house,,true,34,Sierra Leonean-British creative director; Editor-in-Chief Dazed; Prada/Valentino collaborations
lotta_volkova,Lotta,Lotta Volkova,real,stylist;creative_director,summer_house,,true,42,Russian-born stylist/creative director; independent; Paris-based; European summer circuit
dovile_drizyte,Dovile,Dovile Drizyte,real,casting_director;fashion_industry,summer_house,,true,38,Lithuanian casting director; Prada/Miu Miu/McQueen campaigns; invisible infrastructure
etienne_moreau,Étienne,Étienne Moreau,fictional_supporting,chef,hatfield_nyc,,true,42,Executive Chef at The Stave NYC (Tribeca); French-trained (Le Cordon Bleu; staged at Pierre Gagnaire Paris; CDC at Daniel before Hatfield recruited him 2022); runs The Stave NYC kitchen and oversees private dining at West 71st when Alex hosts; quiet professional; Alex knows him well
princess_isabella_savoy,Princess Isabella,HRH Princess Isabella Maria Teresa of Savoy-Aosta,fictional_supporting,royal;deceased,family,,false,,"Alex's maternal great-grandmother (Richard Dawson's mother); Italian royal, cadet branch of House of Savoy-Aosta; born Turin 1918; came to London during WWII; married Archibald Dawson 6th Earl of Fletching 1945; died 2005; gave the Fletching line direct Italian royal descent"
prince_ludovico_savoy,Prince Ludovico,HRH Prince Ludovico of Savoy-Aosta,fictional_supporting,royal;deceased,family,,false,,"Alex's maternal great-great-grandfather; fictional cadet of Savoy-Aosta branch; father of Princess Isabella; born 1888 died 1960; remained in Italy through the house's deposition 1946"
princess_anastasia_greece,Princess Anastasia,HRH Princess Anastasia Sophia of Greece and Denmark,fictional_supporting,royal;deceased,family,,false,,"Alex's maternal great-grandmother (Margaret Dawson's mother); Greek royal, cadet branch of House of Glücksburg; born Athens 1924; evacuated to London 1941 after German invasion of Greece; married General Sir Edward Whitelock 1948; died 2001; gave Margaret direct Greek royal descent and connects the family to the Mountbatten/Windsor cousin web via Prince Philip's Greek-royal lineage"
edward_whitelock,Sir Edward,General Sir Edward Whitelock GCB MC,fictional_supporting,military;deceased,family,,false,,"Alex's maternal great-grandfather (Margaret Dawson's father); British Army officer; served North Africa and Italy WWII; knighted 1962; married Princess Anastasia of Greece and Denmark 1948; died 1998; father of Margaret Whitelock who became Countess of Fletching on marriage to 7th Earl"
```

---

## Source: `data_places.csv` {#data-places-csv}

### Columns

| Column |
|---|
| `id` |
| `name` |
| `city` |
| `region_or_state` |
| `country` |
| `type` |
| `ownership` |
| `access_tier` |
| `first_appearance` |
| `sensory_file` |
| `skill_reference` |
| `notes` |

### Preview

| id | name | city | region_or_state | country | type | ownership | access_tier | first_appearance | sensory_file | skill_reference | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| phoenix_hollow | Phoenix Hollow Compound | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  | prose/places/phoenix_hollow.md | worldguide-keeneland | ~500 acres; ~$56M; 50+ room main house + 8 guest cottages; sleeps ~60 overnight; primary home for Rosie/Homer; Alex's home base; private gate is the line; Summer/Winter Solstice venue — see prose/setpieces/solstice_party.md |
| wilson_sound_studio | Wilson Sound Studio | Versailles | Woodford County KY | USA | studio | wilson_family_owned | compound_only |  |  |  | ~2400sqft; Neve console; Homer-designed acoustics; built 1982; 2-3 min walk from main house; never gone quiet |
| phoenix_hollow_cottage_stone | Stone House Guest Cottage | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  |  |  | Most private cottage; for working artists; isolation focus; one of eight guest cottages |
| phoenix_hollow_cottage_creek | Creek Cottage | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  |  |  | Stevie Nicks's preferred cottage; near the water; quieter than others; one of eight guest cottages |
| phoenix_hollow_cottage_ridge | Ridgeline Cottage | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  |  |  | Dolly Parton's favourite; higher ground; views over the paddocks; one of eight guest cottages |
| phoenix_hollow_cottage_new | The New Place Guest Cottage | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  |  |  | Most modern of the eight guest cottages |
| phoenix_hollow_cottage_dogwood | Dogwood Cottage | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  |  |  | Closest cottage to main house; smaller/family-scale; Cosima's go-to when she doesn't want the main suite; one of eight guest cottages |
| phoenix_hollow_cottage_pond | Pond House | Versailles | Woodford County KY | USA | compound | wilson_family_owned | compound_only |  |  |  | Overlooks the pond; songwriter-favourite; very quiet; porch over the water; one of eight guest cottages |

### Full CSV

```csv
id,name,city,region_or_state,country,type,ownership,access_tier,first_appearance,sensory_file,skill_reference,notes
phoenix_hollow,Phoenix Hollow Compound,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,prose/places/phoenix_hollow.md,worldguide-keeneland,~500 acres; ~$56M; 50+ room main house + 8 guest cottages; sleeps ~60 overnight; primary home for Rosie/Homer; Alex's home base; private gate is the line; Summer/Winter Solstice venue — see prose/setpieces/solstice_party.md
wilson_sound_studio,Wilson Sound Studio,Versailles,Woodford County KY,USA,studio,wilson_family_owned,compound_only,,,,~2400sqft; Neve console; Homer-designed acoustics; built 1982; 2-3 min walk from main house; never gone quiet
phoenix_hollow_cottage_stone,Stone House Guest Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Most private cottage; for working artists; isolation focus; one of eight guest cottages
phoenix_hollow_cottage_creek,Creek Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Stevie Nicks's preferred cottage; near the water; quieter than others; one of eight guest cottages
phoenix_hollow_cottage_ridge,Ridgeline Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Dolly Parton's favourite; higher ground; views over the paddocks; one of eight guest cottages
phoenix_hollow_cottage_new,The New Place Guest Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Most modern of the eight guest cottages
phoenix_hollow_cottage_dogwood,Dogwood Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Closest cottage to main house; smaller/family-scale; Cosima's go-to when she doesn't want the main suite; one of eight guest cottages
phoenix_hollow_cottage_pond,Pond House,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Overlooks the pond; songwriter-favourite; very quiet; porch over the water; one of eight guest cottages
phoenix_hollow_cottage_paddock,The Paddock Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Near the equestrian center; used for horse-crowd guests during Keeneland weeks — owners, trainers, bloodstock agents; one of eight guest cottages
phoenix_hollow_cottage_oakhill,Oak Hill Cottage,Versailles,Woodford County KY,USA,compound,wilson_family_owned,compound_only,,,,Oldest structure on the property; 1880s tenant farmer's house, preserved and quietly renovated; where Willie lands when he's through; one of eight guest cottages
west_71st_nyc,West 71st Street Townhouse,New York City,New York,USA,townhouse,wilson_family_owned,inner_circle,,prose/places/west_71st_nyc.md,,6-story brownstone; ~14000sqft; 8 bed; ~$22M; UWS; 5 blocks from Lincoln Center; AW Assets
kensington_london,Kensington Townhouse,London,Greater London,UK,townhouse,wilson_family_owned,inner_circle,,prose/places/kensington.md,,Upper Phillimore Gardens W8; double-fronted Victorian; 6 floors; ~£37M; Homer's house; AW Assets
villa_serena,Villa Serena,Porto Cervo,Sardinia,Italy,villa,wilson_family_owned,inner_circle,,prose/places/villa_serena.md,worldguide-sardinia,Costa Smeralda; 4 hectares; private cove; ~$70M; 5 guest pavilions; AW Assets; no pap access to cove
laurel_canyon_la,Laurel Canyon House,Los Angeles,California,USA,compound,wilson_family_owned,inner_circle,,prose/places/laurel_canyon.md,,Mid-century modernist; ~$45M; Walker Holdings; Rosie/Homer 1967-1980; home studio; where The Circle formed
fletching_park,Fletching Park,Haywards Heath,East Sussex,UK,compound,leased_regularly,invite_only,,,,2800 acres; Earl of Fletching seat since 1690s; Georgian house; Alex visited twice; maternal grandfather's estate
hatfield_distillery,Hatfield Distillery,Bardstown,Nelson County KY,USA,compound,industry,vip_bookable,,,,Original Hatfield whiskey distillery; Homer's 1978 origin; cave programme; Carolyn Hatfield-Moore
hatfield_still_house,Hatfield Still House,Bardstown,Nelson County KY,USA,restaurant,industry,vip_bookable,,,,James Beard Award restaurant; Marcus Boyle; Bardstown fine dining; bourbon pairing
hatfield_lexington,Hatfield Bar & Grill — Lexington,Lexington,Woodford County KY,USA,restaurant,industry,public,,,,Flagship Hatfield B&G; local Sayre Boys venue; bourbon programme
hatfield_stave_london,The Stave (London),Soho,Greater London,UK,club,industry,member_only,,,,Homer-specified listening room; Quad electrostatics; most perfect club listening room in London
hatfield_stave_nyc,The Stave (NYC),Tribeca,New York,USA,club,industry,member_only,,prose/places/the_stave_nyc.md,,NYC outpost of The Stave private members club; Tribeca (Franklin St); Homer-specified listening room; Étienne Moreau Exec Chef; 400-member cap
hatfield_inns_bardstown,Hatfield Inn — Bardstown,Bardstown,Nelson County KY,USA,hotel,industry,vip_bookable,,,,Boutique Hatfield Inn; bourbon integration; 8-hotel chain anchor
hatfield_inns_lexington,Hatfield Inn — Lexington,Lexington,Woodford County KY,USA,hotel,industry,vip_bookable,,,,Hatfield Inn; Woodford County base
hatfield_inns_london,Hatfield Inn — London,London,Greater London,UK,hotel,industry,vip_bookable,,,,Hatfield Inn; London outpost; bourbon programme
keeneland,Keeneland Race Course,Lexington,Woodford County KY,USA,racecourse,public,public,,prose/places/keeneland.md,worldguide-keeneland,Two meets/year (spring/fall); ~600M annual economic impact; Alex grew up attending; Keeneland Club members-only
carnegie_hall,Carnegie Hall,New York City,New York,USA,venue,public,public,,,,Alex performed Oct 2025; Juilliard world; ~2804 seats; one of world's great concert halls
wigmore_hall,Wigmore Hall,London,Greater London,UK,venue,public,public,,,,Alex performed Dec 2025; classical music's most intimate major venue; London's Juilliard equivalent
royal_albert_hall,Royal Albert Hall,London,Greater London,UK,venue,public,public,,,,5272 capacity; Proms etc; Alex's future London concert possibility
juilliard_school,The Juilliard School,New York City,New York,USA,school,industry,public,,,,Lincoln Center campus; Alex's BM 2022-2025; Dr. Marlowe; John Erskine Prize
royal_academy_of_music,Royal Academy of Music,London,Greater London,UK,school,industry,public,,,,RAM; Alex's junior year exchange 2023-24; Homer lectures here; Alex's London formation
sayre_school,Sayre School,Lexington,Woodford County KY,USA,school,industry,public,,,,Alex's K-10 school; Sayre Boys formed here; Woodford County elite school
westminster_school,Westminster School,London,Greater London,UK,school,industry,public,,,,Alex's sixth form 2019-2021; Jonathan/Lucas Dawson connection; Westminster Boys chat origin
glastonbury,Glastonbury Festival,Pilton,Somerset,UK,festival_site,public,public,,prose/places/glastonbury.md,real-world-reference,Alex's birthday June 22 2025; crowd absorption disperses pap pack; 200000 attendees; Tipi Suites access
zero_bond,Zero Bond,New York City,New York,USA,club,frequented,member_only,,,,NYC private members club; Alex's downtown social life; Juilliard/celebrity crossover
annabels,Annabel's,London,Greater London,UK,club,frequented,member_only,,,,Berkeley Square; London's pre-eminent private members club; London Lot social anchor
chiltern_firehouse,Chiltern Firehouse,London,Greater London,UK,hotel,frequented,vip_bookable,,,,Marylebone; restaurant and hotel; London celebrity circuit; not Alex's default but occasional
casa_cipriani_ny,Casa Cipriani,New York City,New York,USA,club,frequented,member_only,,,,Governors Island private members club; NY social infrastructure
la_terrazza_porto_cervo,La Terrazza Restaurant,Porto Cervo,Sardinia,Italy,restaurant,frequented,public,,,,Physical anchor of summer social world; where the La Terrazza chat gets its name; staff know everyone
billboards_ibiza,Ibiza Town/Sant Antoni club circuit,Ibiza Town,Ibiza,Spain,venue,frequented,vip_bookable,,worldguide-european-summer,Ibiza summer circuit; Edo's world; medium pap situation; villa hills give cover
guards_polo_club,Guards Polo Club,Windsor,Berkshire,UK,venue,frequented,member_only,,,,August polo season; where Alex played Aug 2025; royal/aristocratic world; Hugo Manners crossover
sayre_lake_house,Herrington Lake House,Herrington Lake,Mercer County KY,USA,compound,frequented,inner_circle,,,,Crawford family lake house; standing tradition; poker/fishing/horses; Tommy/Sayre Boys territory
cahill_farm,Cahill Farm,Woodford County,Kentucky,USA,compound,frequented,inner_circle,,,,Sayre Boys territory; lake weekends; bourbon country backdrop
metropolitan_museum,Metropolitan Museum of Art,New York City,New York,USA,gallery,public,public,,,,Met Gala venue; Alex is 2026 co-chair; Young Met Board member; annual Met Gala since age 10
teterboro,Teterboro Airport,Teterboro,New Jersey,USA,airport,frequented,private,,real-world-reference,NYC private aviation hub; Alex's departures from NYC
farnborough,Farnborough Airport,Farnborough,Hampshire,UK,airport,frequented,private,,real-world-reference,London private aviation hub; Alex's UK departures
```

---

## Source: `data_relationships.csv` {#data-relationships-csv}

### Columns

| Column |
|---|
| `from_id` |
| `to_id` |
| `relation_type` |
| `since` |
| `strength` |
| `information_access` |
| `notes` |

### Preview

| from_id | to_id | relation_type | since | strength | information_access | notes |
| --- | --- | --- | --- | --- | --- | --- |
| alex_wilson | rosie_walker | parent | 2003-06-22 | 5 | full_insider | Legal mother; raised from birth; calls her Mama |
| alex_wilson | homer_wilson | parent | 2003-06-22 | 5 | full_insider | Legal father; raised from birth; calls him Papa or Dad |
| alex_wilson | eleanor_vance | professional_advisor | birth | 4 | full_insider | Childhood family friend; manages his world since birth; he trusts her completely |
| alex_wilson | tommy_crawford | best_friend | 2009 | 5 | full_insider | Best friend since kindergarten; no performance; 21 years of shorthand; T-Bone |
| alex_wilson | elton_john | godparent | 2003-06-22 | 3 | partial_insider | Godfather; decades-long Rosie/Homer friend; periodic compound; loud-affection elder |
| alex_wilson | chris_martin | godparent | 2003-06-22 | 3 | partial_insider | Godfather; Apple's father; low-drama practical; intermittent but stable family contact |
| alex_wilson | donatella_versace | godparent | 2003-06-22 | 3 | partial_insider | Godmother; calls him Alexander; high-conviction aesthetic authority; Milan-fashion channel |
| alex_wilson | stella_mccartney | godparent | 2003-06-22 | 3 | partial_insider | Godmother; Stella McCartney fashion house; values-forward style advisor; London-based |

### Full CSV

```csv
from_id,to_id,relation_type,since,strength,information_access,notes
alex_wilson,rosie_walker,parent,2003-06-22,5,full_insider,Legal mother; raised from birth; calls her Mama
alex_wilson,homer_wilson,parent,2003-06-22,5,full_insider,Legal father; raised from birth; calls him Papa or Dad
alex_wilson,eleanor_vance,professional_advisor,birth,4,full_insider,Childhood family friend; manages his world since birth; he trusts her completely
alex_wilson,tommy_crawford,best_friend,2009,5,full_insider,Best friend since kindergarten; no performance; 21 years of shorthand; T-Bone
alex_wilson,elton_john,godparent,2003-06-22,3,partial_insider,Godfather; decades-long Rosie/Homer friend; periodic compound; loud-affection elder
alex_wilson,chris_martin,godparent,2003-06-22,3,partial_insider,Godfather; Apple's father; low-drama practical; intermittent but stable family contact
alex_wilson,donatella_versace,godparent,2003-06-22,3,partial_insider,Godmother; calls him Alexander; high-conviction aesthetic authority; Milan-fashion channel
alex_wilson,stella_mccartney,godparent,2003-06-22,3,partial_insider,Godmother; Stella McCartney fashion house; values-forward style advisor; London-based
alex_wilson,apple_martin,sibling_close,birth,4,partial_insider,God-sister; sibling-close NOT romantic; born May 14 2004; Sardinia connection; normalizes the summer world for Alex
alex_wilson,moses_martin,sibling_close,birth,2,partial_insider,God-sibling; Chris/Gwyneth's son; god-siblings chat member
alex_wilson,zachary_furnish_john,sibling_close,2010,2,partial_insider,God-sibling; Elton's son; god-siblings chat member
alex_wilson,elijah_furnish_john,sibling_close,2013,2,partial_insider,God-sibling; Elton's son; god-siblings chat member
alex_wilson,cody_ashford,best_friend,2009,3,partial_insider,Sayre Boys core; high-volume catalyst; Woodford County; maintained through London/NY years
alex_wilson,jake_patterson,best_friend,2009,3,partial_insider,Sayre Boys core; logistics-first; horse/land expertise; minimal communication
alex_wilson,danny_harlan,best_friend,2009,3,partial_insider,Sayre Boys core; dry irony; arrives late with exact perfect line
alex_wilson,nadia_hassani,professional_advisor,2024,4,full_insider,EA; manages all logistics; London-based; Eleanor hired her; daily operational partner
alex_wilson,kevin_marsh,professional_advisor,2023,3,full_insider,CPO; ex-USSS; 2 years together; separate basement room in NYC townhouse; knows Alex's movements
alex_wilson,sophie_kalu,professional_advisor,2025-01,3,partial_insider,PA; hired early 2025 under Nadia; Nigerian-British; operational support
alex_wilson,james_latham,professional_advisor,2025-06,3,partial_insider,Head of AL.X; manages all inbound; enforces blacklist; Scooter banned; ZERO chat access
alex_wilson,maria_santos,family_friend,birth,4,full_insider,Compound chef; knows Alex since childhood; family-level warmth
alex_wilson,dale_shackleford,family_friend,birth,3,full_insider,Estate manager; compound institution; Woodford County family connection
alex_wilson,loretta_mae,family_friend,birth,3,full_insider,Compound household manager; Rosie/Homer PA; maternal warmth
alex_wilson,jim_crawford,family_friend,childhood,3,partial_insider,Tommy's father; father figure to Alex; no performative awe; Crawford Construction
alex_wilson,darlene_crawford,family_friend,childhood,3,partial_insider,Tommy's mother; fed Alex approximately 10000 meals; practical maternal warmth
alex_wilson,richard_dawson,family_friend,2019,2,public_only,Maternal grandfather; Earl of Fletching; Westminster reconnection age 16; measured relationship
alex_wilson,margaret_dawson,family_friend,2019,2,public_only,Maternal grandmother; Countess; asks about Rosie; holds Dawson emotional architecture
alex_wilson,jonathan_dawson,family_friend,2019,3,partial_insider,First cousin; Westminster School; measured affection; Dawson Cousins chat anchor
alex_wilson,lucas_ashby,family_friend,2019,3,partial_insider,First cousin once removed; easier friendship; Notting Hill; warmest Dawson connection; texts more than Jonathan
alex_wilson,brandi_carlile,mentor,childhood,3,partial_insider,Annual compound residency; like older sister; practical modern-career mentor; craft-specific coaching
alex_wilson,stevie_nicks,mentor,birth,3,partial_insider,De facto aunt/godmother figure; Phoenix Hollow Circle; story-led artistic elder
alex_wilson,dolly_parton,mentor,birth,3,partial_insider,De facto aunt; blunt practical counsel; grounded craft elder
alex_wilson,beyonce,industry_peer,childhood,2,partial_insider,Phoenix Hollow Circle; strategic clarity; sparse presence but significant when she appears
alex_wilson,adele,industry_peer,childhood,2,partial_insider,Phoenix Hollow Circle; blunt warmth; wrote half of 25 at compound
alex_wilson,lady_gaga,industry_peer,childhood,2,partial_insider,Phoenix Hollow Circle; story-first framework; conceptual presence
alex_wilson,taylor_swift,industry_peer,childhood,2,partial_insider,Phoenix Hollow Circle; ghost/lurker in Summer House chat; not close personally
alex_wilson,paul_mccartney,mentor,birth,2,partial_insider,Long-view musical benchmark; quiet validator; compound visits
alex_wilson,joni_mitchell,mentor,birth,2,partial_insider,High-rigor artistic truth voice; Rosie's peer; occasional compound presence
alex_wilson,david_gilmour,family_friend,birth,2,partial_insider,Homer's closest friend; Pink Floyd; craft-first minimal talker
alex_wilson,dr_catherine_marlowe,mentor,2022-09,3,partial_insider,Juilliard piano professor; John Erskine Prize; "Best undergraduate recital in twenty years"
alex_wilson,dr_amara_osei,mentor,2022-09,2,partial_insider,Juilliard voice faculty; pushing Alex toward voice training post-graduation
alex_wilson,nora_yoon,best_friend,2022-09,3,partial_insider,Juilliard peer; real friend; Korean-American; direct musical honesty; NY Lot
alex_wilson,marcus_delacroix,best_friend,2022-09,3,partial_insider,Juilliard peer; nightlife energy; all-caps NYC summons; NY Lot
alex_wilson,freddie_ashworth,best_friend,2019,3,partial_insider,Westminster School peer; London Lot execution engine; Thursday plans
alex_wilson,jess_okonkwo,best_friend,2019,3,partial_insider,Westminster/London peer; music discovery voice; Wigmore-adjacent
alex_wilson,cosima_hicks,best_friend,2019,3,partial_insider,Artist; sculptor; London Lot; made Sound & Bone piece for Alex's NYC bedroom
alex_wilson,hugo_manners,best_friend,2019,3,partial_insider,Westminster peer; London Lot country/polo lane; Guards Polo Club world
alex_wilson,tommaso_corsini,best_friend,2023,3,partial_insider,La Terrazza anchor; Milan/Sardinia; genuine peer friendship; authentic
alex_wilson,edo_ferretti,best_friend,2023,2,partial_insider,La Terrazza chaos anchor; DJ/promoter; Ibiza/Sardinia connection
alex_wilson,camille_aubert,industry_peer,2023,2,partial_insider,Parisian gallerist; La Terrazza; connects Alex to art world perspective
alex_wilson,lucia_montero,best_friend,2023,2,partial_insider,La Terrazza; sharp/political; genuine intellectual friendship
alex_wilson,vittoria_ceretti,confirmed_hookup,2025-07,1,public_only,Confirmed hookup Sardinia July/Aug 2025; Daily Mail front page
alex_wilson,taylor_russell,confirmed_hookup,2025-10,1,partial_insider,Carnegie Hall after-party Oct 2025; one_photo evidence; Page Six
alex_wilson,hunter_schafer,rumored_hookup,2025-09,1,partial_insider,Paris Fashion Week Sept 2025; strongly_suspected; DeuxMoi sourced
alex_wilson,addison_rae,rumored_hookup,2025-09,1,partial_insider,NYC-Paris FW Sept 2025; strongly_suspected; DeuxMoi sourced
alex_wilson,alix_earle,rumored_hookup,2025-07,1,public_only,Ibiza July 2025; rumor only; DeuxMoi sourced
alex_wilson,dove_cameron,rumored_hookup,2025-06,1,public_only,London June 2025; rumor only; DeuxMoi sourced
rosie_walker,homer_wilson,parent,1970,5,full_insider,Married 1971; met Abbey Road 1970; 55 years together; the greatest partnership
rosie_walker,eleanor_vance,family_friend,1985,4,full_insider,Niece figure; Margaret Vance's daughter; Rosie calls her "my niece"; complete trust
rosie_walker,elton_john,collaborator,1970,4,partial_insider,Phoenix Hollow Circle; decades friendship; godparent to Alex; Circle anchor
rosie_walker,david_gilmour,collaborator,1970,3,partial_insider,Pink Floyd connection through Homer; Phoenix Hollow presence
homer_wilson,elton_john,collaborator,1973,3,partial_insider,Engineered Honky Château and Goodbye Yellow Brick Road; Phoenix Hollow Circle
homer_wilson,david_gilmour,best_friend,1970,4,partial_insider,Closest friend; Pink Floyd Pink Floyd Floyd work; writes letters; annual visits
```

---

## Source: `data_chat_memberships.csv` {#data-chat-memberships-csv}

### Columns

| Column |
|---|
| `person_id` |
| `chat_id` |
| `chat_name` |
| `posting_frequency` |
| `tone_note` |

### Preview

| person_id | chat_id | chat_name | posting_frequency | tone_note |
| --- | --- | --- | --- | --- |
| alex_wilson | fam | FAM — Family | high | Daily check-in; reacts quickly to Rosie; answers Eleanor directly; no performance register |
| rosie_walker | fam | FAM — Family | high | Sets emotional texture; dawn garden photos; short song lines; irregular porch voice notes |
| homer_wilson | fam | FAM — Family | low | Goes silent for days then returns with dry non-sequiturs; low-frequency signal |
| eleanor_vance | fam | FAM — Family | medium | Logistics and decisions; clear yes/no asks; warmth appears briefly around milestones |
| alex_wilson | sayre_boys | SB — Sayre Boys | high | Bridge between worlds; very active; matches local cadence; drops out-of-context global details |
| tommy_crawford | sayre_boys | SB — Sayre Boys | high | Compression + punchlines; short replies; dry escalation; would rather be mauled by horse than admit he reads Phoenix Hollow chat |
| cody_ashford | sayre_boys | SB — Sayre Boys | high | High-volume catalyst; multi-text bursts; all-caps when excited |
| jake_patterson | sayre_boys | SB — Sayre Boys | low | Posts rarely; horses/land/transport specifics; logistics-first |

### Full CSV

```csv
person_id,chat_id,chat_name,posting_frequency,tone_note
alex_wilson,fam,FAM — Family,high,Daily check-in; reacts quickly to Rosie; answers Eleanor directly; no performance register
rosie_walker,fam,FAM — Family,high,Sets emotional texture; dawn garden photos; short song lines; irregular porch voice notes
homer_wilson,fam,FAM — Family,low,Goes silent for days then returns with dry non-sequiturs; low-frequency signal
eleanor_vance,fam,FAM — Family,medium,Logistics and decisions; clear yes/no asks; warmth appears briefly around milestones
alex_wilson,sayre_boys,SB — Sayre Boys,high,Bridge between worlds; very active; matches local cadence; drops out-of-context global details
tommy_crawford,sayre_boys,SB — Sayre Boys,high,Compression + punchlines; short replies; dry escalation; would rather be mauled by horse than admit he reads Phoenix Hollow chat
cody_ashford,sayre_boys,SB — Sayre Boys,high,High-volume catalyst; multi-text bursts; all-caps when excited
jake_patterson,sayre_boys,SB — Sayre Boys,low,Posts rarely; horses/land/transport specifics; logistics-first
danny_harlan,sayre_boys,SB — Sayre Boys,medium,Arrives after reading full thread; lands exact understated line; late precision
alex_wilson,london_lot,LL — London Lot,medium,Amplifies activity when physically in London; dry understatement; plan-confirming energy
freddie_ashworth,london_lot,LL — London Lot,high,Execution engine; suggests plan; converts vague interest into attendance
hugo_manners,london_lot,LL — London Lot,medium,Country/polo lane activator; activates countryside branch
cosima_hicks,london_lot,LL — London Lot,medium,Art/culture selector; dry tone; often early/right on trends
jess_okonkwo,london_lot,LL — London Lot,medium,Music discovery; RAM-adjacent curation; Wigmore-adjacent
jonathan_dawson,london_lot,LL — London Lot,low,Low-frequency anchor; complete sentences; reflective posts; quieter end of LL
lucas_ashby,london_lot,LL — London Lot,medium,Casual warmth; architecture enthusiasm; faster social response than Jonathan
raye,london_lot,LL — London Lot,medium,British music energy; gig/event focused
stormzy,london_lot,LL — London Lot,low,Grime authority; low frequency when he appears it matters
central_cee,london_lot,LL — London Lot,low,UK rap; low frequency
tom_holland,london_lot,LL — London Lot,medium,British actor; London base; social presence
florence_pugh,london_lot,LL — London Lot,medium,British actress; London social life; active in LL when home
paul_mescal,london_lot,LL — London Lot,low,Irish actor; London-adjacent; occasional presence
iris_law,london_lot,LL — London Lot,medium,Creative/photographer; art world London connection
lila_moss,london_lot,LL — London Lot,medium,Fashion world; Kate's daughter; London social anchor
lady_amelia_windsor,london_lot,LL — London Lot,medium,Aristocratic fashion; royal-adjacent; London Season anchor
olympia_of_greece,london_lot,LL — London Lot,medium,Greek/Danish royal; London/NY crossover; fashion presence
alex_wilson,westminster_boys,WB — Westminster Boys,medium,Routinely mocked for American angle; belongs fully; inside-joke register
freddie_ashworth,westminster_boys,WB — Westminster Boys,high,Core voice; Westminster 2019-2021 cohort; laddish roast energy
hugo_manners,westminster_boys,WB — Westminster Boys,high,Core voice; polo/country references; school-specific callbacks
alex_wilson,ny_lot,NYL — New York Lot,medium,Active but not usually the originator; downtown momentum energy
marcus_delacroix,ny_lot,NYL — New York Lot,high,Declarative nightlife launch; all-caps summons energy; 9PM NOT OPTIONAL
nora_yoon,ny_lot,NYL — New York Lot,medium,Culture-program proposer; concerts/recitals over generic drinks; Juilliard anchor
derrick_washington,ny_lot,NYL — New York Lot,low,Late-night specialist; appears after 10pm; studio sessions
sasha_volkov,ny_lot,NYL — New York Lot,low,Low frequency; concise interest signals; violin world
jin_park,ny_lot,NYL — New York Lot,low,Terse progress updates; cellist world
henry_cabot,ny_lot,NYL — New York Lot,medium,Table access and venue leverage; hosts with social capital
sam_okafor,ny_lot,NYL — New York Lot,medium,Bridge node between Juilliard and club ecosystems
timothee_chalamet,ny_lot,NYL — New York Lot,low,French-American; downtown NYC crossover; piano player energy
zoe_kravitz,ny_lot,NYL — New York Lot,low,Zero Bond crowd; Legacy Admissions crossover
alex_wilson,legacy_admissions,LA — Legacy Admissions,medium,Stabilizing voice; crisis handling moves to DM; self-aware funny about inherited absurdity
apple_martin,legacy_admissions,LA — Legacy Admissions,high,Core daily energy; Chris/Gwyneth's daughter; normalizing summer world for Alex
lila_moss,legacy_admissions,LA — Legacy Admissions,medium,Fashion world legacy; Kate's daughter
rocco_ritchie,legacy_admissions,LA — Legacy Admissions,low,Madonna/Guy's son; own summer circuit; lower frequency
iris_law,legacy_admissions,LA — Legacy Admissions,medium,Creative world; Jude's daughter
maya_hawke,legacy_admissions,LA — Legacy Admissions,medium,Uma/Ethan's daughter; Hudson Valley/LA crossover
lennon_gallagher,legacy_admissions,LA — Legacy Admissions,medium,Liam's son; fashion/music world; British base
anais_gallagher,legacy_admissions,LA — Legacy Admissions,medium,Noel's daughter; fashion world; British base
damian_hurley,legacy_admissions,LA — Legacy Admissions,medium,Elizabeth's son; British model/actor
kaia_gerber,legacy_admissions,LA — Legacy Admissions,medium,Cindy's daughter; LA/NY crossover; model world
jack_schlossberg,legacy_admissions,LA — Legacy Admissions,low,JFK's grandson; political/cultural legacy; seasonal tourist energy
zoe_kravitz,legacy_admissions,LA — Legacy Admissions,low,Lenny's daughter; NY base; Legacy crossover
timothee_chalamet,legacy_admissions,LA — Legacy Admissions,low,Considered legacy-adjacent through French artistic family; occasional presence
alex_wilson,summer_house,SH — Summer House,medium,Confirms plans Nadia has prepped; medium-chaos energy; seasonal peak
apple_martin,summer_house,SH — Summer House,high,Core presence; god-sister; Sardinia anchor
lila_moss,summer_house,SH — Summer House,high,Location switchboard; tracks where people actually are
rocco_ritchie,summer_house,SH — Summer House,medium,Has own circuit; overlaps Glastonbury and European stops
iris_law,summer_house,SH — Summer House,medium,Creative world; summer circuit presence
lady_amelia_windsor,summer_house,SH — Summer House,medium,Young Royals tier; aristocratic fashion presence
samuel_chatto,summer_house,SH — Summer House,low,Young Royals tier; low-key artist; periodic presence
arthur_chatto,summer_house,SH — Summer House,low,Young Royals tier; lower presence
lennon_gallagher,summer_house,SH — Summer House,medium,British summer circuit; fashion/music world
anais_gallagher,summer_house,SH — Summer House,medium,British summer circuit; fashion world
damian_hurley,summer_house,SH — Summer House,medium,British summer circuit; model/actor
maya_hawke,summer_house,SH — Summer House,medium,Legacy bridge; Hudson Valley/LA/European crossover
timothee_chalamet,summer_house,SH — Summer House,low,NY/London extras tier; seasonal overlap
barry_keoghan,summer_house,SH — Summer House,low,Irish actor; NY/London extras; seasonal
freddie_ashworth,summer_house,SH — Summer House,medium,London Lot bridge into Summer House; summer plans
nora_yoon,summer_house,SH — Summer House,low,Juilliard crossover; summer circuit when in Europe
marcus_delacroix,summer_house,SH — Summer House,low,Juilliard crossover; summer circuit when relevant
jacob_elordi,summer_house,SH — Summer House,medium,Core voice; minimal post maximal effect; seasonal peak
emma_chamberlain,summer_house,SH — Summer House,high,High-volume chaos accelerator; spiral posting style
sabrina_carpenter,summer_house,SH — Summer House,medium,Sharp thread closer; fast last-word tendency
jenna_ortega,summer_house,SH — Summer House,low,Low-frequency impact; single-line dry hits
tommaso_corsini,summer_house,SH — Summer House,medium,La Terrazza bridge into Summer House; Sardinia logistics
edo_ferretti,summer_house,SH — Summer House,medium,Ibiza/summer energy; chaos accelerator in peak periods
camille_aubert,summer_house,SH — Summer House,low,Paris-side; seasonal summer presence
zendaya,summer_house,SH — Summer House,ghost_only,Ghost/lurker; high-signal when she rarely posts
taylor_swift,summer_house,SH — Summer House,ghost_only,Ghost/lurker; presence acknowledged by others
beyonce,summer_house,SH — Summer House,ghost_only,Ghost/lurker; rare appearance; room-shifting energy
olivia_rodrigo,summer_house,SH — Summer House,low,Seasonal tourist; summer circuit overlap
jeremy_allen_white,summer_house,SH — Summer House,low,Seasonal tourist; London/NYC overlap
austin_butler,summer_house,SH — Summer House,low,Seasonal tourist; occasional presence
princess_maria_olympia,summer_house,SH — Summer House,medium,Young Royals tier; Greek/Danish royal; fashion world
princess_alexia,summer_house,SH — Summer House,low,Young Royals tier; Dutch royal; lower presence
achileas_of_greece,summer_house,SH — Summer House,medium,Young Royals tier; Greek/Danish; Mediterranean circuit
olympia_of_greece,summer_house,SH — Summer House,medium,Young Royals tier; London/NY crossover; fashion
naomi_campbell,summer_house,SH — Summer House,low,Fashion week bridge; Glastonbury presence; periodic appearance
harry_styles,summer_house,SH — Summer House,low,Summer circuit crossover; periodic presence
dua_lipa,summer_house,SH — Summer House,low,Summer circuit crossover; periodic presence
florence_pugh,summer_house,SH — Summer House,medium,British Power Anchor; London summer circuit
anya_taylor_joy,summer_house,SH — Summer House,low,British-Argentine; summer circuit crossover
paul_mescal,summer_house,SH — Summer House,medium,Irish actor; British Power Anchor
tom_holland,summer_house,SH — Summer House,medium,British actor; British Power Anchor
stormzy,summer_house,SH — Summer House,low,Glastonbury/summer circuit presence; British Power Anchor
central_cee,summer_house,SH — Summer House,low,UK rap; British Power Anchor; seasonal
raye,summer_house,SH — Summer House,medium,British music; summer circuit; Glastonbury connection
alex_wilson,la_terrazza,LT — La Terrazza,medium,More expansive in Italian-register exchanges; genuine peer in this world
tommaso_corsini,la_terrazza,LT — La Terrazza,high,Anchor; consistency; architecture/food/travel blend; calm planner
edo_ferretti,la_terrazza,LT — La Terrazza,medium,Late-night instigator; improbable plans that often execute
camille_aubert,la_terrazza,LT — La Terrazza,medium,Aesthetic/editorial lens; dry precision; Paris-side filtering
lucia_montero,la_terrazza,LT — La Terrazza,medium,Political/intellectual edge; brings links/opinions/questions from Madrid
felix_arnoult,la_terrazza,LT — La Terrazza,medium,Wine/food/history enthusiasm; concrete specificity over persona gimmick
giulia_agnelli,la_terrazza,LT — La Terrazza,low,Fashion-world intermittent presence; in-and-out; low-fuss; Tommaso-connected
alex_wilson,dawson_cousins,DC — Dawson Cousins,low,Present without forcing intensity; shows care by showing up; London overlap triggers
jonathan_dawson,dawson_cousins,DC — Dawson Cousins,medium,Initiator and continuity; formal grammar; quiet warmth; chat existence part of repair
lucas_ashby,dawson_cousins,DC — Dawson Cousins,medium,Faster social response; casual warmth; architecture enthusiasm
beatrice_dawson,dawson_cousins,DC — Dawson Cousins,low,Edinburgh counterpoint; sardonic/direct; lower posting frequency
rosie_walker,phoenix_hollow,PH — Phoenix Hollow,high,Centre of gravity; sets tone; primary social architect of the space
homer_wilson,phoenix_hollow,PH — Phoenix Hollow,medium,Backbone presence; studio updates; compound logistics; occasional dry non-sequiturs
eleanor_vance,phoenix_hollow,PH — Phoenix Hollow,low,Family-adjacent continuity; family business; operational information
alex_wilson,phoenix_hollow,PH — Phoenix Hollow,medium,Family presence; active but not dominant; genuine compound member
tommy_crawford,phoenix_hollow,PH — Phoenix Hollow,read_only,Has never once posted; reads every message; would rather be mauled by horse than admit it
elton_john,phoenix_hollow,PH — Phoenix Hollow,medium,Circle anchor; loud-affection energy; periodic compound posts; declares things
stevie_nicks,phoenix_hollow,PH — Phoenix Hollow,medium,Image-rich reflective phrasing; unhurried narrative arcs; emotional continuity
dolly_parton,phoenix_hollow,PH — Phoenix Hollow,medium,Warm plainspoken directness; affectionate address; Nashville thread anchor
paul_mccartney,phoenix_hollow,PH — Phoenix Hollow,low,Long-view minimal posts; often photos with no captions; intermittent high-impact
david_gilmour,phoenix_hollow,PH — Phoenix Hollow,low,Work-over-words; craft-specific; Homer-adjacent presence
joni_mitchell,phoenix_hollow,PH — Phoenix Hollow,low,Less frequent but major-presence; high-rigor artistic truth; Rosie's peer
brandi_carlile,phoenix_hollow,PH — Phoenix Hollow,medium,Contemporary bridge generation; actively mentoring; practical modern-career voice
beyonce,phoenix_hollow,PH — Phoenix Hollow,low,Sparse weighted lines; strategic clarity; low frequency high significance
adele,phoenix_hollow,PH — Phoenix Hollow,low,Blunt warmth; occasional appearances; wrote half of 25 at compound
lady_gaga,phoenix_hollow,PH — Phoenix Hollow,low,Conceptual but concrete; framework language; crisp idea-dense when present
taylor_swift,phoenix_hollow,PH — Phoenix Hollow,low,Inner Circle status; relatively low-frequency in PH chat; masters advice recipient
chris_martin,phoenix_hollow,PH — Phoenix Hollow,low,Low-drama practical; intermittent family contact; Apple's father
stella_mccartney,phoenix_hollow,PH — Phoenix Hollow,low,Style authority; periodic posts; London-based
donatella_versace,phoenix_hollow,PH — Phoenix Hollow,low,High-conviction aesthetic commands; Milan-centric; Italian fashion authority
bruce_springsteen,phoenix_hollow,PH — Phoenix Hollow,low,Legacy anchor; periodic presence; compound visitor
jack_white,phoenix_hollow,PH — Phoenix Hollow,low,Compound residency visits; studio-focused
alicia_keys,phoenix_hollow,PH — Phoenix Hollow,low,Homer-produced album connection; compound visits
billie_eilish,phoenix_hollow,PH — Phoenix Hollow,low,Contemporary generation crossover; compound visitor
harry_styles,phoenix_hollow,PH — Phoenix Hollow,low,British fashion/music crossover; world stage presence
kate_moss,phoenix_hollow,PH — Phoenix Hollow,low,Legacy parent tier; Lila's mother; occasional presence
david_beckham,phoenix_hollow,PH — Phoenix Hollow,low,Global crossover; fashion and sports world; compound visits; couple presence
victoria_beckham,phoenix_hollow,PH — Phoenix Hollow,low,Fashion authority; VB label founder; design world; compound visits; couple presence
madonna,phoenix_hollow,PH — Phoenix Hollow,low,Legacy parent tier; Rocco's mother; icon presence
jude_law,phoenix_hollow,PH — Phoenix Hollow,low,Legacy parent tier; Iris's father; actor world
gwyneth_paltrow,phoenix_hollow,PH — Phoenix Hollow,low,Legacy parent tier; Apple's mother; Goop/wellness adjacent
lenny_kravitz,phoenix_hollow,PH — Phoenix Hollow,low,Music world; Apple's godfather; compound visitor
lila_moss,phoenix_hollow,PH — Phoenix Hollow,low,Legacy Core; Phoenix Hollow member; summer circuit crossover
rocco_ritchie,phoenix_hollow,PH — Phoenix Hollow,low,Legacy Core; Phoenix Hollow member; own summer circuit
iris_law,phoenix_hollow,PH — Phoenix Hollow,low,Legacy Core; Phoenix Hollow member; creative/art world
lady_amelia_windsor,phoenix_hollow,PH — Phoenix Hollow,low,Legacy Core; Phoenix Hollow member; aristocratic fashion
samuel_chatto,phoenix_hollow,PH — Phoenix Hollow,low,Legacy Core; Phoenix Hollow member; Princess Margaret connection
arthur_chatto,phoenix_hollow,PH — Phoenix Hollow,low,Legacy Core; Phoenix Hollow member; low-key presence
barack_obama,phoenix_hollow,PH — Phoenix Hollow,ghost_only,Low-frequency; when he posts the room shifts; compound visitor presence
michelle_obama,phoenix_hollow,PH — Phoenix Hollow,ghost_only,Low-frequency; public figures tier; compound visitor
chad_smith,phoenix_hollow,PH — Phoenix Hollow,medium,Nashville Backbone; session work at compound; operational chat texture
steve_jordan,phoenix_hollow,PH — Phoenix Hollow,medium,Nashville Backbone; Rolling Stones touring drummer; session work
pino_palladino,phoenix_hollow,PH — Phoenix Hollow,medium,Nashville Backbone; session bassist; compound sessions
paul_franklin,phoenix_hollow,PH — Phoenix Hollow,medium,Nashville Backbone; steel guitar; Nashville institution
maria_santos,phoenix_hollow,PH — Phoenix Hollow,low,Nashville Backbone; compound chef; mentioned more than she posts (her food is legend)
dale_shackleford,phoenix_hollow,PH — Phoenix Hollow,low,Nashville Backbone; estate manager; compound logistics
tyrone_lebon,summer_house,SH — Summer House,low,Editorial photographer; rarely posts; occasional Milan/Paris presence noted
cass_bird,summer_house,SH — Summer House,ghost_only,NY-based; follows; documents when present; never posts
morgan_maassen,summer_house,SH — Summer House,low,Seasonal July-August; surf/boat texture; occasional photo drop
campbell_addy,summer_house,SH — Summer House,medium,London crossover; Burberry-adjacent; European summer when work permits
ibrahim_kamara,summer_house,SH — Summer House,low,Milan/Paris circuit; professional orbit with social crossover
lotta_volkova,summer_house,SH — Summer House,low,Paris-based; rare posts; physically present more than digitally active
dovile_drizyte,summer_house,SH — Summer House,ghost_only,Industry infrastructure; follows; never posts; knows everyone
ice_spice,summer_house,SH — Summer House,low,Seasonal tourist; July-August peak; Bronx/NYC energy
```

---

## Source: `data_aliases.csv` {#data-aliases-csv}

### Columns

| Column |
|---|
| `person_id` |
| `alias` |
| `alias_type` |
| `used_by` |
| `notes` |

### Preview

| person_id | alias | alias_type | used_by | notes |
| --- | --- | --- | --- | --- |
| alex_wilson | AL.X | alter_ego | public | The fashion/luxury-world facing brand identity; AL.X is the professional management division name |
| alex_wilson | @alexwilson23 | stage_name | public | Instagram handle; 95M+ followers as of Jan 2026 |
| alex_wilson | Alexander | nickname | inner_circle | Used exclusively by Donatella Versace; never by anyone else |
| alex_wilson | Alex Wilson | stage_name | public | DG recording artist name; IMG model name; public identity |
| rosie_walker | Mama | nickname | inner_circle | Alex's private name for Rosie; used only by him |
| rosie_walker | Mrs. Wilson | nickname | inner_circle | Used in Woodford County; compound staff and local community |
| rosie_walker | Rosie | nickname | inner_circle | Used by old friends and peers; not "Grandma" not "Grandmother" |
| rosie_walker | Rosie Walker | stage_name | public | Public performing name; full legal name is Rosie Walker Wilson |

### Full CSV

```csv
person_id,alias,alias_type,used_by,notes
alex_wilson,AL.X,alter_ego,public,The fashion/luxury-world facing brand identity; AL.X is the professional management division name
alex_wilson,@alexwilson23,stage_name,public,Instagram handle; 95M+ followers as of Jan 2026
alex_wilson,Alexander,nickname,inner_circle,Used exclusively by Donatella Versace; never by anyone else
alex_wilson,Alex Wilson,stage_name,public,DG recording artist name; IMG model name; public identity
rosie_walker,Mama,nickname,inner_circle,Alex's private name for Rosie; used only by him
rosie_walker,Mrs. Wilson,nickname,inner_circle,Used in Woodford County; compound staff and local community
rosie_walker,Rosie,nickname,inner_circle,Used by old friends and peers; not "Grandma" not "Grandmother"
rosie_walker,Rosie Walker,stage_name,public,Public performing name; full legal name is Rosie Walker Wilson
homer_wilson,Papa,nickname,inner_circle,Alex's private name for Homer; also uses "Dad" interchangeably
homer_wilson,Sir Homer,nickname,public,Post-1998 KBE; formal address in professional contexts
homer_wilson,Dad,nickname,inner_circle,Alex uses "Dad" interchangeably with "Papa"
eleanor_vance,Eleanor,nickname,inner_circle,All inner circle use full name; no diminutive
tommy_crawford,T-Bone,nickname,inner_circle,Alex's private nickname for Tommy; used only between them; 21 years of history encoded
tommy_crawford,Tommy,nickname,inner_circle,Universal; all Sayre Boys and family
elton_john,Elton,nickname,inner_circle,Universal; all circle members
elton_john,Sir Elton,nickname,public,Post-knighthood formal address
donatella_versace,Nella,nickname,inner_circle,Alex's name for Donatella; used only by him and possibly Homer/Rosie
stella_mccartney,Stella,nickname,inner_circle,Universal; both her fashion house and personal name
brandi_carlile,Brandi,nickname,inner_circle,Universal; Circle and close friends
david_gilmour,David G,nickname,inner_circle,To distinguish from Jonathan Dawson's David; Homer's usage
tommy_crawford,Crawford,nickname,inner_circle,Used by other Sayre Boys sometimes; regional Kentucky register
cody_ashford,Cody,nickname,inner_circle,Universal; Sayre Boys
jake_patterson,Jake,nickname,inner_circle,Universal; Sayre Boys
danny_harlan,Danny,nickname,inner_circle,Universal; Sayre Boys
nadia_hassani,Nadia,nickname,inner_circle,Universal; Alex and team
kevin_marsh,Kevin,nickname,inner_circle,How Alex addresses him; "Shadow" in Pinned contacts
kevin_marsh,Shadow,nickname,inner_circle,Alex's pinned contact name for Kevin in iPhone; reference to constant protective presence
james_latham,Latham,nickname,inner_circle,How Eleanor and Alex refer to him in business contexts
apple_martin,Apple,nickname,inner_circle,Universal; god-sibling; Chris Martin/Gwyneth's daughter
richard_dawson,The Earl,nickname,inner_circle,How the Dawson family refers to him; Alex uses it privately
jonathan_dawson,Jonathan,nickname,inner_circle,Universal in London Lot and Dawson Cousins chat
lucas_ashby,Lucas,nickname,inner_circle,Universal in London Lot
freddie_ashworth,Freddie,nickname,inner_circle,Universal; London Lot
vittoria_ceretti,Vittoria,nickname,public,Stage/professional name; Italian supermodel
addison_rae,Addison,nickname,public,Content creator; public persona name
alix_earle,Alix,nickname,public,Content creator; public persona name
tommaso_corsini,Tommaso,nickname,inner_circle,Universal; La Terrazza
edo_ferretti,Edo,nickname,inner_circle,Universal; short for Edoardo; La Terrazza
```

---

## Source: `data_business_deals.csv` {#data-business-deals-csv}

### Columns

| Column |
|---|
| `id` |
| `person_id` |
| `deal_type` |
| `counterparty` |
| `signed_date` |
| `status` |
| `term_length` |
| `public_knowledge` |
| `announced_date` |
| `public_announcement` |
| `key_terms_summary` |
| `information_wall` |
| `notes` |

### Preview

| id | person_id | deal_type | counterparty | signed_date | status | term_length | public_knowledge | announced_date | public_announcement | key_terms_summary | information_wall | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deal_001 | alex_wilson | recording_contract | Deutsche Grammophon | 2025-06-27 | active | two_album | true | 2025-07-01 | Press release via Walker Holdings / Askonas Holt — international classical debut | Two-album deal. Album I (Diventando..) delivered Aug 2025. Album II (Le Occasioni) in pre-production. Full classical programming — no crossover terms. DG classical roster. Royalty terms confidential. | AL.X team has deal overview. Personal financial terms: family office only. | DG A&R contact reached out via Askonas Holt March 2025. Eleanor negotiated. Better terms than DG expected to give. Walker Records retains consultation rights per Homer's arrangement. |
| deal_002 | alex_wilson | fashion_ambassador | Versace | 2025-08 | active | multi_season | true | 2025-09-01 | Announced via brand and Versace social channels — pre-NYFW | Non-exclusive ambassador. Campaign and show front row. Donatella called personally — not standard practice for any signing. | AL.X team (James Latham) manages. Personal chat access: zero. | Donatella ("Nella") is godmother — relationship predates deal by 20 years. Negotiated to ensure brand compatibility with DG classical positioning. Fits luxury-only scope for AL.X. |
| deal_003 | alex_wilson | fashion_ambassador | Stella McCartney | 2025-08 | active | multi_season | true | 2025-09-01 | Joint announcement with Versace in NYFW context — coordinated by James Latham | Non-exclusive ambassador. Stella is godmother — deal formalised what was already a family relationship. Campaign TBD. | AL.X team manages. Personal chat access: zero. | Stella involved in vetting other fashion house deals to ensure no brand conflicts. The only godparent who is also a direct brand partner. |
| deal_004 | alex_wilson | fashion_ambassador | Dior | 2025-09 | active | multi_season | true | 2025-10-01 | Announced post-Paris Fashion Week September 2025 | Non-exclusive ambassador. Dior menswear focus. Campaign and exclusivity window agreed. Stella McCartney aware and signed off on non-conflict basis. | AL.X team manages. | Third fashion house. Stella diplomatically informed before signing. The picture of Stella and Alex arriving together at a Dior show in March 2026 is intentional brand narrative. |
| deal_005 | alex_wilson | fashion_ambassador | Loewe | 2025-09 | active | multi_season | true | 2025-10-01 | Announced alongside Dior in October 2025 | Non-exclusive ambassador. Loewe brand aesthetics align strongly with classical music positioning — arts-forward luxury. | AL.X team manages. | James Latham's preferred deal from the five — brand identity most aligned with Alex's artistic positioning. Strong campaign creative expected for 2026. |
| deal_006 | alex_wilson | fashion_ambassador | Burberry | 2025-10 | active_pre_campaign | multi_season | true | 2025-11-01 | Signing announced Nov 2025 but campaign images not yet released at story open | Signed deal. Campaign shoot scheduled April 2026. Campaign goes live post-shoot April 18 2026. The last of the five houses to activate publicly. | AL.X team manages. | Ryan flag: Burberry is signed but not yet live at story open (January 2026). Campaign shoot April 10 2026. Launch April 18 2026 — this is a story-arc moment when all 5 houses are live simultaneously. |
| deal_007 | alex_wilson | modelling_contract | IMG Models | 2025-08 | active | rolling | true | 2025-08-15 | Announced via IMG and WME joint statement | IMG Models via WME contract structure. Non-exclusive. Fashion week bookings and editorial coordinated through James Latham and Oliver Wren. | AL.X team manages. WME talent side separate from IMG. | Signed at same time as first fashion houses. WME handles talent; IMG handles model bookings. Priya Chandra runs day-to-day coordination with IMG. |
| deal_008 | alex_wilson | brand_ambassador | Hatfield Group (including Limestone Springs) | 2025-07 | active | multi_year | true | 2025-07-15 | Announced via Hatfield Group PR and Walker Holdings — domestic US coverage | Family business brand ambassador. Covers Hatfield Group brands including Limestone Springs Beverage Co. Bourbon and lifestyle positioning. Domestic US focus (not international luxury scope). | Walker Holdings / Eleanor manages. AL.X team not involved — family business lane. | Deal structure is family-internal. Different from the five fashion houses — this is Rosie's business empire. Alex is the face of Hatfield in US domestic contexts. Limestone Springs is the lead activation product for his non-bourbon positioning (under-21 audience etc). |

### Full CSV

```csv
id,person_id,deal_type,counterparty,signed_date,status,term_length,public_knowledge,announced_date,public_announcement,key_terms_summary,information_wall,notes
deal_001,alex_wilson,recording_contract,Deutsche Grammophon,2025-06-27,active,two_album,true,2025-07-01,Press release via Walker Holdings / Askonas Holt — international classical debut,Two-album deal. Album I (Diventando..) delivered Aug 2025. Album II (Le Occasioni) in pre-production. Full classical programming — no crossover terms. DG classical roster. Royalty terms confidential.,AL.X team has deal overview. Personal financial terms: family office only.,DG A&R contact reached out via Askonas Holt March 2025. Eleanor negotiated. Better terms than DG expected to give. Walker Records retains consultation rights per Homer's arrangement.
deal_002,alex_wilson,fashion_ambassador,Versace,2025-08,active,multi_season,true,2025-09-01,Announced via brand and Versace social channels — pre-NYFW,Non-exclusive ambassador. Campaign and show front row. Donatella called personally — not standard practice for any signing.,AL.X team (James Latham) manages. Personal chat access: zero.,Donatella ("Nella") is godmother — relationship predates deal by 20 years. Negotiated to ensure brand compatibility with DG classical positioning. Fits luxury-only scope for AL.X.
deal_003,alex_wilson,fashion_ambassador,Stella McCartney,2025-08,active,multi_season,true,2025-09-01,Joint announcement with Versace in NYFW context — coordinated by James Latham,Non-exclusive ambassador. Stella is godmother — deal formalised what was already a family relationship. Campaign TBD.,AL.X team manages. Personal chat access: zero.,Stella involved in vetting other fashion house deals to ensure no brand conflicts. The only godparent who is also a direct brand partner.
deal_004,alex_wilson,fashion_ambassador,Dior,2025-09,active,multi_season,true,2025-10-01,Announced post-Paris Fashion Week September 2025,Non-exclusive ambassador. Dior menswear focus. Campaign and exclusivity window agreed. Stella McCartney aware and signed off on non-conflict basis.,AL.X team manages.,Third fashion house. Stella diplomatically informed before signing. The picture of Stella and Alex arriving together at a Dior show in March 2026 is intentional brand narrative.
deal_005,alex_wilson,fashion_ambassador,Loewe,2025-09,active,multi_season,true,2025-10-01,Announced alongside Dior in October 2025,Non-exclusive ambassador. Loewe brand aesthetics align strongly with classical music positioning — arts-forward luxury.,AL.X team manages.,James Latham's preferred deal from the five — brand identity most aligned with Alex's artistic positioning. Strong campaign creative expected for 2026.
deal_006,alex_wilson,fashion_ambassador,Burberry,2025-10,active_pre_campaign,multi_season,true,2025-11-01,Signing announced Nov 2025 but campaign images not yet released at story open,Signed deal. Campaign shoot scheduled April 2026. Campaign goes live post-shoot April 18 2026. The last of the five houses to activate publicly.,AL.X team manages.,Ryan flag: Burberry is signed but not yet live at story open (January 2026). Campaign shoot April 10 2026. Launch April 18 2026 — this is a story-arc moment when all 5 houses are live simultaneously.
deal_007,alex_wilson,modelling_contract,IMG Models,2025-08,active,rolling,true,2025-08-15,Announced via IMG and WME joint statement,IMG Models via WME contract structure. Non-exclusive. Fashion week bookings and editorial coordinated through James Latham and Oliver Wren.,AL.X team manages. WME talent side separate from IMG.,Signed at same time as first fashion houses. WME handles talent; IMG handles model bookings. Priya Chandra runs day-to-day coordination with IMG.
deal_008,alex_wilson,brand_ambassador,Hatfield Group (including Limestone Springs),2025-07,active,multi_year,true,2025-07-15,Announced via Hatfield Group PR and Walker Holdings — domestic US coverage,Family business brand ambassador. Covers Hatfield Group brands including Limestone Springs Beverage Co. Bourbon and lifestyle positioning. Domestic US focus (not international luxury scope).,Walker Holdings / Eleanor manages. AL.X team not involved — family business lane.,Deal structure is family-internal. Different from the five fashion houses — this is Rosie's business empire. Alex is the face of Hatfield in US domestic contexts. Limestone Springs is the lead activation product for his non-bourbon positioning (under-21 audience etc).
deal_009,alex_wilson,institutional_role,Metropolitan Museum of Art — Young Met Board,2024-01,active,ongoing,true,2024-01,Public board membership — announced Met at time of appointment,Young Met Board member since January 2024 (pre-story). Met Gala co-chair announced December 10 2025 for May 2026 ceremony. Non-compensated board role.,Walker Holdings / Eleanor coordinates with Met. Not AL.X scope.,Alex has attended every Met Gala since age 10. Young Met Board is consistent with classical music + fashion positioning. Co-chair is significant — requires substantial preparation and Eleanor involvement Q1 2026.
deal_010,alex_wilson,talent_agency,WME (William Morris Endeavor),2025-06,active,rolling,false,2025-06-27,Not publicly announced as standalone — part of the DG/IMG announcement context,Full-service talent representation. Covers: concerts + touring (coordinated with Askonas Holt), IMG modelling contract structure, brand deal legal, speaking engagements (if any). WME is the external structural framework within which AL.X operates.,AL.X team interfaces with WME. Personal terms: family office only.,James Latham and Eleanor manage the WME relationship. Askonas Holt retains classical concert booking — WME does not override this lane. The two agencies have territorial division agreed.
deal_011,alex_wilson,concert_agency,Askonas Holt,2025-06,active,rolling,false,,Not publicly announced as standalone,Classical concert booking exclusively. Carnegie Hall (Oct 2025) and Wigmore Hall (Dec 2025) booked through Askonas Holt. Future dates including potential 2026 tour TBD.,Family office / Eleanor only.,Premier classical concert agency (represent Lang Lang etc). Retained their lane over WME for classical bookings per deal structure. Homer Wilson recommended them.
deal_012,alex_wilson,pr_firm,The Lede Company,2025-07,active,rolling,false,,Not publicly announced,Personal PR — press strategy for classical + fashion + public persona. Works alongside James Latham and Karla Otto. Sensitivity map enforced — Scooter Braun blacklisted.,AL.X team / James Latham interface only.,Senior partner assigned. Not the same as fashion PR (Karla Otto handles fashion specifically). The Lede handles classical press relationships and broader narrative strategy.
deal_013,alex_wilson,pr_firm,Karla Otto,2025-09,active,rolling,false,,Not publicly announced,Fashion PR specifically — show attendance, press access, fashion editorial strategy. Works alongside The Lede. Fashion week logistics and fashion press relationships.,AL.X team / Oliver Wren interface primarily.,Fashion-specific. Does not have access to classical PR strategy or personal life. Clear lane separation enforced by James Latham.
```
