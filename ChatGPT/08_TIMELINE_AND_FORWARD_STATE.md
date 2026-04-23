# Timeline and Forward State

This file groups the timeline-heavy CSV datasets with the narrative forward-state document so future triggers and background chronology live in one place.

## Included Sources

- `data_calendar_2025_background.csv`
- `data_calendar_2026.csv`
- `data_discography.csv`
- `data_media_coverage_timeline.csv`
- `data_wilson_hookup_tracker.csv`
- `archive_FORWARD_STATE.md`

---

## Source: `data_calendar_2025_background.csv` {#data-calendar-2025-background-csv}

### Columns

| Column |
|---|
| `date` |
| `event` |
| `location_id` |
| `participants` |
| `public_knowledge` |
| `tabloid_source` |
| `narrative_weight` |
| `alex_pov_summary` |

### Preview

| date | event | location_id | participants | public_knowledge | tabloid_source | narrative_weight | alex_pov_summary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-05-22 | Juilliard Commencement — BM Piano Performance conferred; John Erskine Prize announced | juilliard_school | alex_wilson;dr_catherine_marlowe;rosie_walker;homer_wilson | true | NYPost;Billboard | load_bearing | Graduation; everything changes from this moment; Rosie and Homer in the audience |
| 2025-05-22 | The dam breaks — Eleanor fields first wave of post-graduation industry calls |  | eleanor_vance;james_latham | false |  | load_bearing | Industry has been waiting 4 years; Latham in seat holding the door |
| 2025-06-04 | Tribeca Film Festival begins — Alex begins NYC circuit month |  | alex_wilson;nadia_hassani;kevin_marsh | true | PageSix;DailyMail | context | Red carpets; first major public post-graduation appearances; tabloid machinery activates fully |
| 2025-06-15 | Tribeca Film Festival ends — Alex attends multiple premieres and events |  | alex_wilson | true | DailyMail;PageSix;TMZ | context | Two weeks of intensive NYC public appearances; pap baseline established for new era |
| 2025-06-17 | Milan Men's Fashion Week opens — Alex arrives Milan for MFW |  | alex_wilson;donatella_versace;kevin_marsh;nadia_hassani | true | DailyMail;Vogue;BoF | load_bearing | First Fashion Week appearance post-graduation; Donatella in home territory; Versace deal context |
| 2025-06-17 | DG (Deutsche Grammophon) deal negotiations begin — meetings in Milan parallel to MFW |  | alex_wilson;eleanor_vance;james_latham | false |  | load_bearing | Two-album classical deal; rush timeline required to hit Grammy eligibility cutoff |
| 2025-06-22 | Alex's 22nd birthday — celebrated at Glastonbury |  | alex_wilson;apple_martin;lila_moss;rosie_walker | true | DailyMail;TheS;PageSix | context | Birthday June 22 (CC-01 correction); Glastonbury context; Summer House chat peaks |
| 2025-06-22 | Milan MFW ends — fashion house deal discussions accelerate |  | alex_wilson;donatella_versace;stella_mccartney | false |  | context | Multiple house conversations happening in parallel with DG album talks |

### Full CSV

```csv
date,event,location_id,participants,public_knowledge,tabloid_source,narrative_weight,alex_pov_summary
2025-05-22,Juilliard Commencement — BM Piano Performance conferred; John Erskine Prize announced,juilliard_school,alex_wilson;dr_catherine_marlowe;rosie_walker;homer_wilson,true,NYPost;Billboard,load_bearing,Graduation; everything changes from this moment; Rosie and Homer in the audience
2025-05-22,The dam breaks — Eleanor fields first wave of post-graduation industry calls,,eleanor_vance;james_latham,false,,load_bearing,Industry has been waiting 4 years; Latham in seat holding the door
2025-06-04,Tribeca Film Festival begins — Alex begins NYC circuit month,,alex_wilson;nadia_hassani;kevin_marsh,true,PageSix;DailyMail,context,Red carpets; first major public post-graduation appearances; tabloid machinery activates fully
2025-06-15,Tribeca Film Festival ends — Alex attends multiple premieres and events,,alex_wilson,true,DailyMail;PageSix;TMZ,context,Two weeks of intensive NYC public appearances; pap baseline established for new era
2025-06-17,Milan Men's Fashion Week opens — Alex arrives Milan for MFW,,alex_wilson;donatella_versace;kevin_marsh;nadia_hassani,true,DailyMail;Vogue;BoF,load_bearing,First Fashion Week appearance post-graduation; Donatella in home territory; Versace deal context
2025-06-17,DG (Deutsche Grammophon) deal negotiations begin — meetings in Milan parallel to MFW,,alex_wilson;eleanor_vance;james_latham,false,,load_bearing,Two-album classical deal; rush timeline required to hit Grammy eligibility cutoff
2025-06-22,Alex's 22nd birthday — celebrated at Glastonbury,,alex_wilson;apple_martin;lila_moss;rosie_walker,true,DailyMail;TheS;PageSix,context,Birthday June 22 (CC-01 correction); Glastonbury context; Summer House chat peaks
2025-06-22,Milan MFW ends — fashion house deal discussions accelerate,,alex_wilson;donatella_versace;stella_mccartney,false,,context,Multiple house conversations happening in parallel with DG album talks
2025-06-25,Glastonbury Festival begins,,alex_wilson;apple_martin;lila_moss;stormzy,true,DailyMail;TheS;NME,context,Crowd absorption; medium pap situation; Summer House chat peak chaos
2025-06-27,DG deal signed — two-album classical recording contract,,alex_wilson;eleanor_vance;james_latham,false,,load_bearing,Signed in London post-Glastonbury; rush release planned to hit Sept 1 Grammy cutoff
2025-06-29,Glastonbury Festival ends,glastonbury,alex_wilson,true,,context,Post-festival; transition to European summer circuit
2025-07-01,Ibiza — one week stretch with La Terrazza and Summer House crowd,ibiza_circuit,alex_wilson;edo_ferretti;tommaso_corsini;alix_earle,true,DeuxMoi;DailyMail,context,Alix Earle rumour originates here; Edo's world; medium pap situation
2025-07-07,Ibiza stretch ends — travel to Sardinia,,alex_wilson;kevin_marsh,true,DailyMail,context,End of Ibiza week
2025-07-08,Villa Serena Sardinia — three weeks begin,villa_serena,alex_wilson;tommaso_corsini;edo_ferretti;camille_aubert;lucia_montero;felix_arnoult;apple_martin,false,,load_bearing,Most private extended stay of the year; private cove; Vogue shoot arranged here; album mixing in parallel in London
2025-07-10,Vittoria Ceretti arrives Villa Serena — hookup begins,villa_serena,alex_wilson;vittoria_ceretti,false,,load_bearing,Confirmed hookup; Daily Mail photographer eventually gets Porto Cervo transit shot
2025-07-15,Vogue photoshoot — Annie Leibovitz shoots Alex at Villa Serena for September cover,,alex_wilson;vittoria_ceretti;annie_leibovitz,false,,load_bearing,Shot in and around Porto Cervo and Villa Serena; September 2025 British/American Vogue cover
2025-07-22,DM publishes first Ceretti-Wilson photos — Porto Cervo transit shot,la_terrazza_porto_cervo,alex_wilson;vittoria_ceretti,true,DailyMail,load_bearing,First confirmed tabloid photo; "Alex Wilson and Vittoria Ceretti spotted in Porto Cervo"; hookup confirmed
2025-07-29,Villa Serena stay ends — travel back through London,villa_serena,alex_wilson,true,DailyMail,context,Three weeks done; heading to August events
2025-08-01,DG Album I recording sessions begin — London (Air Studios),,,alex_wilson;homer_wilson,false,,load_bearing,Homer engineering; uses Juilliard recital programme; rush production to hit August 22 release
2025-08-05,Guards Polo Club — August polo season,,alex_wilson;hugo_manners,true,DailyMail;HelloMag,context,Alex plays polo August; Guards Polo Club; aristocratic summer season; royal/London crossover
2025-08-20,Dove Cameron rumour surfaces,,alex_wilson;dove_cameron,true,DeuxMoi,context,London context; DeuxMoi sourced; rumour only
2025-08-22,Album I released — "Alex Wilson — Album I — Diventando.." on Deutsche Grammophon,,alex_wilson;homer_wilson,true,Billboard;NYT;Guardian;Telegraph,load_bearing,Rush release 8 days before Grammy cutoff; Juilliard recital programme; Bach+Beethoven+Prokofiev+Liszt; global classical/crossover coverage
2025-08-22,DG Album I global press campaign launches,,alex_wilson;james_latham;priya_chandra,true,NYT;Guardian;FT;NYorker;Billboard,load_bearing,Classical press + crossover press; Homer's name adds engineering credibility; Grammy whispers begin immediately
2025-09-01,Grammy eligibility cutoff — Album I qualifies for 68th Grammys,,,,false,,load_bearing,Made it; 8-day margin
2025-09-01,Vogue September issue hits — Alex Wilson cover story,,alex_wilson;annie_leibovitz,true,Vogue;DailyMail;TheS;Instagram,load_bearing,British/American Vogue simultaneous; September issue; Annie Leibovitz shots; breakout cultural moment
2025-09-05,AL.X management division fully operational — Latham in seat with full team,,james_latham;priya_chandra;oliver_wren,false,,context,AL.X managing all inbound; Scooter blacklist enforced; information wall absolute
2025-09-10,Versace deal activated — first campaign content begins,,alex_wilson;donatella_versace,true,Vogue;WWD;BoF,load_bearing,First fashion house campaign live; Donatella's project
2025-09-12,Stella McCartney deal activated,,alex_wilson;stella_mccartney,true,Vogue;WWD,context,Second fashion house campaign; Stella's values-forward aesthetic
2025-09-15,New York Fashion Week — Alex attends shows; seated front row at multiple houses,,alex_wilson;nadia_hassani;kevin_marsh,true,Vogue;WWD;BoF;DailyMail,context,NYFW appearances; seated for Versace/Stella and others; pap situation elevated; Hunter Schafer seen at same shows
2025-09-22,Paris Fashion Week begins — Alex in Paris for PFW,,alex_wilson;donatella_versace;hunter_schafer;addison_rae,true,DailyMail;PageSix;DeuxMoi,context,Hunter Schafer strongly suspected hookup originates here; Addison Rae also in Paris; DeuxMoi activity peaks
2025-09-25,Dior deal signed — third fashion house,,alex_wilson;james_latham,false,,context,Dior non-exclusive ambassador; adds to fashion portfolio
2025-09-27,Loewe deal signed — fourth fashion house,,alex_wilson;james_latham,false,,context,Loewe non-exclusive; Jonathan Anderson relationship
2025-10-01,Paris Fashion Week ends,,alex_wilson,true,DailyMail;DeuxMoi,context,Addison Rae strongly suspected hookup; DeuxMoi sourced NYC-Paris context
2025-10-02,GQ interview published — first major profile,,alex_wilson,true,GQ;DailyMail;Vogue,load_bearing,Major men's magazine profile post-Album I release; covers music + fashion + the summer
2025-10-15,Carnegie Hall performance — solo piano recital; Album I programme,,alex_wilson,true,NYT;Telegraph;Billboard;ClassicalFM,load_bearing,First major concert hall performance post-graduation; 2804 seats; reviewed internationally; Taylor Russell seen at after-party
2025-10-17,Taylor Russell Page Six photo — Carnegie Hall after-party,carnegie_hall,alex_wilson;taylor_russell,true,PageSix,context,One photo; Page Six runs it; "one_photo" evidence; not confirmed beyond image
2025-10-20,Keeneland October Meet — back in Woodford County briefly,,alex_wilson;tommy_crawford;cody_ashford;jake_patterson;danny_harlan,false,,context,Compound time; Keeneland fall meet; Sayre Boys reunion; compound reset
2025-11-01,Burberry deal signed — fifth fashion house (not yet activated),,alex_wilson;james_latham,false,,context,Signed but campaign not started; Burberry ⚠️ status; awaiting campaign launch
2025-11-08,Grammy nominations announced — 68th Grammy Awards,,alex_wilson,true,Billboard;NYT;DailyMail;TMZ,load_bearing,Nominated Best Classical Solo Instrumental Album; Alex Wilson Album I; global coverage; fever pitch
2025-11-15,IMG Models official announcement — signed via WME contract,,alex_wilson;james_latham,true,Vogue;BoF;WWD;DailyMail,load_bearing,IMG Models signing publicly announced; model career formal; reinforces fashion portfolio
2025-11-30,Young Met Board meetings continue — Met Gala 2026 co-chair planning begins,,alex_wilson;eleanor_vance,false,,context,December announcement being prepared; board discussions underway
2025-12-05,Wigmore Hall performance — solo piano recital; London; early December,,alex_wilson,true,Guardian;Telegraph;ClassicalFM;TimesUK,load_bearing,London concert; Wigmore Hall; more intimate than Carnegie; UK press major review
2025-12-10,Met Gala 2026 co-chair announced publicly,,alex_wilson,true,Vogue;DailyMail;NYT;Guardian;WWD,load_bearing,Named as co-chair for May 2026 Met Gala ceremony; first solo co-chair of his generation; enormous media coverage
2025-12-15,Compound for Christmas — Phoenix Hollow,,alex_wilson;rosie_walker;homer_wilson;eleanor_vance;tommy_crawford,false,,context,Winter Solstice party; inner circle; compound as home; year-end review with Eleanor
2025-12-22,Winter Solstice party at Phoenix Hollow — 60-80 inner circle guests,,rosie_walker;homer_wilson;alex_wilson;elton_john;stevie_nicks;dolly_parton;brandi_carlile,false,,context,Annual compound Winter Solstice; inner circle only; no press; Circle present
2025-12-31,Year end — Alex at compound; first January 2026 approaching,,alex_wilson;rosie_walker;homer_wilson,false,,context,Grammy ceremony Feb 2 approaching; opening story state being set
```

---

## Source: `data_calendar_2026.csv` {#data-calendar-2026-csv}

### Columns

| Column |
|---|
| `date` |
| `event` |
| `location_id` |
| `participants` |
| `public_knowledge` |
| `tabloid_source` |
| `narrative_weight` |
| `alex_pov_summary` |
| `status` |
| `trigger_for` |

### Preview

| date | event | location_id | participants | public_knowledge | tabloid_source | narrative_weight | alex_pov_summary | status | trigger_for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-01-05 | Return to NYC from compound after New Year — story staging begins | west_71st_nyc | alex_wilson | false |  | context | Back in New York after compound New Year. Grammys four weeks out. The year already has gravity. | locked_real_world | story_open_baseline |
| 2026-01-08 | AL.X team January briefing — James Latham presents Q1 opportunities triage; Burberry campaign pre-production timeline discussed | west_71st_nyc | alex_wilson,james_latham,priya_chandra,oliver_wren | false |  | context | Eleanor's operation maps Q1. Grammy prep running alongside Burberry pre-production. Alex listens. Asks two questions. Says he'll think about the spring schedule. | locked_real_world | burberry_preproduction_thread |
| 2026-01-12 | Grammy nominee spotlight — DG releases behind-the-scenes clip from Album I recording sessions; 4.2M views in 24hrs | digital | alex_wilson | true | pitchfork_classical | load_bearing | The algorithm runs without him. He watches the clip once and puts his phone down. | locked_real_world | grammy_media_momentum |
| 2026-01-15 | STORY OPEN + CHICKEN SHOP DATE DROPS: Alex at West 71st; Chicken Shop Date episode (Amelia Dimoldenberg) drops without warning or promo; Grammy 18 days out; GQ publishes in 2 days | west_71st_nyc | alex_wilson | true | deuxmoi | load_bearing | The Chicken Shop Date drops today. No warning. He knew it was coming. The Grammy is 18 days away. The apartment is quiet. The internet is not. | locked_real_world | story_begins |
| 2026-01-17 | GQ profile publishes — 'The Classical Kid Arrives'; cover and 8-page spread; shoots from November 2025 | digital | alex_wilson | true | gq_us | load_bearing | He's read it. He doesn't recognise himself entirely but it isn't wrong. Elton texts immediately: "Darling — GQ. Finally." | locked_real_world | gq_reactions_thread |
| 2026-01-20 | Grammy rehearsal week begins — nominee media commitments and press day (Recording Academy protocol) | new_york_city | alex_wilson | true | rolling_stone | context | Two days of press. He does it. Nadia coordinates every minute. | locked_real_world | grammy_press_day_scene |
| 2026-01-24 | Dinner at Zero Bond — NY social circuit; NY Lot crew; Marcus has a table | zero_bond_nyc | alex_wilson,marcus_delacroix,nora_yoon,henry_cabot,timothee_chalamet | false |  | context | Normal evening. Marcus booked it. Henry argued about the wine list. Timothée came late and left early. | proposed | ny_social_scene |
| 2026-01-28 | Recording Academy nominees reception — Grammy week eve; industry dinner; DG table | new_york_city | alex_wilson,dg_label_contact | true | billboard | context | The industry in one room. Alex is polite and moves efficiently. He does not linger. | locked_real_world | industry_pre_grammy_scene |

### Full CSV

```csv
date,event,location_id,participants,public_knowledge,tabloid_source,narrative_weight,alex_pov_summary,status,trigger_for
2026-01-05,Return to NYC from compound after New Year — story staging begins,west_71st_nyc,alex_wilson,false,,context,Back in New York after compound New Year. Grammys four weeks out. The year already has gravity.,locked_real_world,story_open_baseline
2026-01-08,AL.X team January briefing — James Latham presents Q1 opportunities triage; Burberry campaign pre-production timeline discussed,west_71st_nyc,"alex_wilson,james_latham,priya_chandra,oliver_wren",false,,context,Eleanor's operation maps Q1. Grammy prep running alongside Burberry pre-production. Alex listens. Asks two questions. Says he'll think about the spring schedule.,locked_real_world,burberry_preproduction_thread
2026-01-12,Grammy nominee spotlight — DG releases behind-the-scenes clip from Album I recording sessions; 4.2M views in 24hrs,digital,alex_wilson,true,pitchfork_classical,load_bearing,The algorithm runs without him. He watches the clip once and puts his phone down.,locked_real_world,grammy_media_momentum
2026-01-15,STORY OPEN + CHICKEN SHOP DATE DROPS: Alex at West 71st; Chicken Shop Date episode (Amelia Dimoldenberg) drops without warning or promo; Grammy 18 days out; GQ publishes in 2 days,west_71st_nyc,alex_wilson,true,deuxmoi,load_bearing,The Chicken Shop Date drops today. No warning. He knew it was coming. The Grammy is 18 days away. The apartment is quiet. The internet is not.,locked_real_world,story_begins
2026-01-17,GQ profile publishes — 'The Classical Kid Arrives'; cover and 8-page spread; shoots from November 2025,digital,alex_wilson,true,gq_us,load_bearing,"He's read it. He doesn't recognise himself entirely but it isn't wrong. Elton texts immediately: ""Darling — GQ. Finally.""",locked_real_world,gq_reactions_thread
2026-01-20,Grammy rehearsal week begins — nominee media commitments and press day (Recording Academy protocol),new_york_city,alex_wilson,true,rolling_stone,context,Two days of press. He does it. Nadia coordinates every minute.,locked_real_world,grammy_press_day_scene
2026-01-24,Dinner at Zero Bond — NY social circuit; NY Lot crew; Marcus has a table,zero_bond_nyc,"alex_wilson,marcus_delacroix,nora_yoon,henry_cabot,timothee_chalamet",false,,context,Normal evening. Marcus booked it. Henry argued about the wine list. Timothée came late and left early.,proposed,ny_social_scene
2026-01-28,Recording Academy nominees reception — Grammy week eve; industry dinner; DG table,new_york_city,"alex_wilson,dg_label_contact",true,billboard,context,The industry in one room. Alex is polite and moves efficiently. He does not linger.,locked_real_world,industry_pre_grammy_scene
2026-02-02,68th Grammy Awards — Crypto.com Arena Los Angeles; Alex nominated Best Classical Solo Instrumental Album; Homer and Rosie attending as Grammy Legends (annual — Rosie has not released since 1980); staying at Laurel Canyon,crypto_arena_la,"alex_wilson,rosie_walker,homer_wilson,eleanor_vance,kevin_marsh,nadia_hassani",true,grammy_broadcast,load_bearing,"He is nominated. Homer and Rosie are in the room — they go every year, Grammy Legends. This year Alex is also there, as something different. Kevin is on detail. Win or loss: Ryan decides.",player_choice_dependent,grammy_outcome_arc
2026-02-03,Grammy aftermath — Laurel Canyon / LA; Vanity Fair party; industry circuit; Eleanor debrief; Homer and Rosie still in town,los_angeles,"alex_wilson,eleanor_vance",true,vanity_fair,load_bearing,The morning after tells you where the year goes. Homer makes coffee. Rosie does not ask how he feels. Eleanor waits until noon to call.,player_choice_dependent,year_direction_pivot
2026-02-06,Return compound — decompression period; Homer in studio; no public schedule,phoenix_hollow,"alex_wilson,homer_wilson,rosie_walker",false,,context,He needs a week. Homer doesn't say anything. The studio is open.,proposed,compound_decompression_scene
2026-02-14,Valentine's Day — social media ambient attention spikes; tabloid speculation cycle,digital,alex_wilson,true,deuxmoi,trivia,He doesn't post anything. This is itself a story the fan accounts run with for 48 hours.,locked_real_world,tabloid_speculation_ambient
2026-02-20,Burberry campaign concept presentation — London (remote or in-person TBD); first creative meeting for campaign that hasn't yet gone live,london_or_remote,"alex_wilson,james_latham,burberry_team",false,,context,The campaign that's been signed but not shot. First creative session. Alex has opinions about the direction.,proposed,burberry_creative_direction_arc
2026-03-05,Milan Men's Fashion Week — Loewe and Versace shows; Alex front row; AL.X coordination heavy,milan,"alex_wilson,james_latham,kevin_marsh,nadia_hassani",true,vogue_runway,load_bearing,Third fashion week. The routine is established. He knows the photographers by name now. He moves differently through these rooms than he did in September.,locked_real_world,milan_fashion_week_scenes
2026-03-08,Post-MFW dinner — Tommaso Ferrini hosts; La Terrazza core; Camille and Félix fly in,milan,"alex_wilson,tommaso_ferrini,edo_bianchi,camille_laurent,felix_moreau",false,,context,The real Milan. Tommaso's table. No obligations. Someone opened something extraordinary and nobody can remember what.,proposed,european_circle_social_scene
2026-03-15,London — Kensington; Homer at The Stave; Jess Okonkwo Wigmore recommendation; Freddie pub,kensington_london,"alex_wilson,homer_wilson,jess_okonkwo,freddie_ashworth",false,,context,London always feels different from New York. Quieter in the right ways. Homer spends two hours in the listening room with Marcus Boyle.,proposed,kensington_compound_scene
2026-03-20,Paris Fashion Week — Dior and Stella McCartney shows; Stella is godmother so the Dior show is her territory to navigate diplomatically,paris,"alex_wilson,stella_mccartney,james_latham,kevin_marsh",true,vogue_paris,load_bearing,Stella is fully aware of the Dior contract. She was involved in negotiating the terms. The fashion world watches the picture of them arriving together.,locked_real_world,paris_fashion_week_scenes
2026-04-01,Return compound — spring settle; Keeneland Spring Meet in three weeks; Tommy back from wherever Tommy was,phoenix_hollow,"alex_wilson,tommy_crawford",false,,context,He's been away since January with gaps. The compound recalibrates him. Tommy appears on the second day as if he never left.,proposed,compound_spring_reset
2026-04-04,Keeneland Spring Meet begins — annual racing; Alex in Keeneland Club; Sayre Boys crew; industry people; press light relative to London,keeneland,"alex_wilson,tommy_crawford,cody_ashford,jake_patterson,danny_harlan",true,ny_post_gossip,context,This is home-scale famous. Everyone knows him and nobody makes a thing of it. The horses are the point.,locked_real_world,keeneland_spring_scenes
2026-04-04,Le Occasioni (Album II) releases via Deutsche Grammophon — Schubert D.960 / Liszt Bénédiction / Ravel Gaspard / Montale coda; recorded back to back with Album I at compound studio; Homer Wilson producing,digital,"alex_wilson,dg_label_contact,homer_wilson",true,gramophone,load_bearing,The second record is out. DG handles the announcement. Homer is at the compound. Alex does not post anything on release day — the record speaks.,locked_real_world,album_ii_release_arc
2026-04-10,Burberry campaign shoot — London (first live campaign work); location TBD,london,"alex_wilson,kevin_marsh,nadia_hassani",true,,load_bearing,The campaign that's been waiting since the signing. It goes live after this. Something shifts in the public-facing record.,locked_real_world,burberry_campaign_shoot_scene
2026-04-11,"Coachella Weekend 1 — Alex's first ever Coachella (has done Glastonbury many times and other festivals but Coachella always clashed — school, Juilliard, RAM); wearing custom Burberry look designed for the festival; first public images of Alex in Burberry circulate as festival photography before official campaign launch; Sabrina Carpenter headlining; Justin Bieber headlining",coachella_indio,"alex_wilson,kevin_marsh,nadia_hassani",true,daily_mail,load_bearing,His first Coachella. He has watched it from a distance every year — always something in the way. Not this year. The Burberry look is custom. The photos will run everywhere before Karla Otto's team even files the press release.,locked_real_world,coachella_w1_arc
2026-04-12,PRIVATE — PLAYER CHOICE ONLY — DO NOT REFERENCE IN PUBLIC CONTENT OR MEDIA RENDERS: Possibility of surprise stage appearance / guest set during Coachella Weekend 1. Headliners Sabrina Carpenter and Justin Bieber both known to Alex through Circle and Summer House connections. Nature and scope of any appearance: Ryan's call during scene. Information wall: zero public knowledge until played.,coachella_indio,alex_wilson,false,,load_bearing,PRIVATE. This exists in the files. It does not exist in the world until Ryan plays it. Do not telegraph. Do not hint in public-facing renders. Do not write fan accounts anticipating it.,player_choice_dependent,coachella_surprise_performance_arc
2026-04-18,Burberry campaign launches — digital and print; official launch on Coachella Weekend 2; first public images already circulating from Weekend 1; all five fashion houses simultaneously live for the first time,digital,alex_wilson,true,daily_mail,load_bearing,Five houses. All live now. The Weekend 1 photos have been running for a week. Today is when it becomes official. The coverage reframes him — there is a before and after to this image in the public record.,locked_real_world,burberry_public_record_shift
2026-04-18,Coachella Weekend 2 — second weekend; Burberry campaign officially launches same day; five houses simultaneously live; Sabrina Carpenter and Justin Bieber headlining,coachella_indio,"alex_wilson,kevin_marsh,nadia_hassani",true,vogue_runway,load_bearing,Weekend 2. The campaign is live. The photos from Weekend 1 have been everywhere for a week. Today is the official version of something that has already happened. He does not check his phone during the headliner set.,locked_real_world,coachella_w2_arc
2026-05-04,Met Gala — Metropolitan Museum New York; Alex as co-chair (announced Dec 2025); Young Met Board; this is his most prominent public event since the Grammys,metropolitan_museum,"alex_wilson,eleanor_vance,kevin_marsh,nadia_hassani",true,vogue_met_gala,load_bearing,Co-chair. He's been to every one since he was 10 — with Rosie then alone then as someone people watch. This one is different. Eleanor briefs him for three days running.,locked_real_world,met_gala_cochair_arc
2026-05-05,Met Gala aftermath — press cycle peaks; coverage runs for 72 hours; tabloid speculation about companions,digital,alex_wilson,true,daily_mail,load_bearing,The morning after the Met Gala is its own event. He's off his phone until noon.,locked_real_world,met_gala_press_cycle
2026-06-01,European summer planning confirmed — Sardinia June-July; Ibiza brief stop; circuit begins,phoenix_hollow,alex_wilson,false,,context,Eleanor has the schedule. Kevin has the security plan. Nadia has the logistics. Alex has a window.,proposed,european_summer_arc
2026-06-15,Glastonbury Festival — VIP compound; social circuit; 200000 people; pap scale high but crowd absorption applies,glastonbury,"alex_wilson,tommy_crawford,freddie_ashworth,jess_okonkwo",true,daily_mail,context,His birthday four days prior (June 22 — but story time shifts). Glastonbury is chaos and he loves it in a specific way. The scale flattens the hierarchy.,locked_real_world,glastonbury_scenes
2026-06-22,Alex Wilson birthday — 23rd; compound or Sardinia depending on story; quiet preferred,phoenix_hollow_or_villa_serena,alex_wilson,false,,context,He is 23. He makes no announcement. The Circle members text over a 48-hour window. Tommy texts exactly nothing and then appears in person.,locked_real_world,birthday_23_scene
2026-07-01,Villa Serena summer residency begins — Sardinia; La Terrazza core arriving in rotation,villa_serena,"alex_wilson,tommaso_ferrini,edo_bianchi,camille_laurent,lucia_espinoza,felix_moreau,giulia_agnelli",false,,context,The annual reset. The private cove. Tommaso arrives first and the house opens.,proposed,sardinia_summer_arc
2026-07-20,Ibiza circuit stop — brief; social; Ushuaïa or DC10 depending on crew energy,ibiza,"alex_wilson,tommaso_ferrini,edo_bianchi",true,deuxmoi,trivia,Two days. He's done this enough times that it's texture not event.,proposed,ibiza_circuit_scene
2026-09-01,NYFW — September opens; this is the fashion week that reoriented everything in 2025; second year in now,new_york_city,"alex_wilson,james_latham,kevin_marsh",true,vogue_runway,context,Second NYFW. Different scale. He's a fixture now — not a new face.,locked_real_world,nyfw_second_year_scenes
2026-10-01,Keeneland Fall Meet — second annual; Sayre Boys; racing; home circuit,keeneland,"alex_wilson,tommy_crawford,cody_ashford,jake_patterson,danny_harlan",true,ny_post_gossip,context,The fall version. Slightly cooler. The colours are different. The crowd is the same people he grew up with.,locked_real_world,keeneland_fall_scenes
2026-10-15,Carnegie Hall — second solo recital; Le Occasioni programme (Album II material); second Carnegie in 12 months,carnegie_hall,alex_wilson,true,nyt_arts,load_bearing,"The second Carnegie. Album II is out. The programme is Le Occasioni in full. Different weight from the first time — the room knows what to expect now, and he plays into that.",locked_real_world,carnegie_second_recital_arc
2026-11-01,"Grammy eligibility confirmed — Le Occasioni (Album II, April 2026 release) eligible for 69th Grammy Awards; DG and Eleanor flag the window",digital,alex_wilson,false,,context,Le Occasioni released April 2026 — inside the September 1 cutoff. It is eligible. Nobody mentions it to Alex until DG sends a one-line note.,locked_real_world,album_ii_release_timing_decision
2026-12-01,Year-end compound return — Rosie and Homer; Circle Christmas circuit; Woodford County settle,phoenix_hollow,"alex_wilson,rosie_walker,homer_wilson",false,,context,The year closes the same way it opened — with the compound, the quiet, the family. The circle comes through in December rotation as always.,proposed,year_end_compound_scenes
2026-12-31,Year-end — 2026 closes; story continuity open,phoenix_hollow,"alex_wilson,rosie_walker,homer_wilson,tommy_crawford",false,,context,The compound at New Year. Same as every year. Different everything else.,proposed,year_end_continuity_open
```

---

## Source: `data_discography.csv` {#data-discography-csv}

### Columns

| Column |
|---|
| `id` |
| `person_id` |
| `credit_type` |
| `work_title` |
| `artist_name` |
| `release_year` |
| `label` |
| `chart_peak_us` |
| `grammy_awards` |
| `programme_notes` |
| `confidentiality` |
| `notes` |

### Preview

| id | person_id | credit_type | work_title | artist_name | release_year | label | chart_peak_us | grammy_awards | programme_notes | confidentiality | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| disc_001 | rosie_walker | artist | A Still Small Voice | Rosie Walker | 1965 | Atlantic Records | 12 | 0 | Folk Revival / Chamber Folk / Classical-Inflected Singer-Songwriter | public | Debut album. Greenwich Village. Two weeks recorded. Folk chart #1. Multi-Diamond (3x). |
| disc_002 | rosie_walker | artist | Baptized in Bourbon | Rosie Walker | 1968 | Atlantic Records | 1 | 0 | Muscle Shoals Soul / R&B / Gospel-Rock | public | Transformation record. Wexler + The Swampers. 14 weeks #1. Multi-Diamond (6x). Two consecutive #1 singles (Sunday Clothes / Baptized). |
| disc_003 | rosie_walker | artist | Good Girls Go to Heaven | Rosie Walker | 1970 | Atlantic Records | 1 | 1 | Symphonic Rock / Wall of Sound | public | AOY Grammy #1 (1971). Abbey Road. Quincy Jones producer. Homer Wilson engineer — they met during this session. 22 weeks #1. Multi-Diamond (12x). 2.1B streams on lead single. |
| disc_004 | rosie_walker | artist | Neon Cathedral | Rosie Walker | 1971 | Atlantic Records | 1 | 1 | Art Rock / Psychedelic / Concept Album | public | AOY Grammy #2 (1972). Concept album — religion + technology. Influenced Bowie and punk. 18 weeks #1. Multi-Diamond (11x). |
| disc_005 | rosie_walker | artist | Starlight & Steel | Rosie Walker | 1972 | Atlantic Records | 1 | 1 | Glam Rock / Hard Rock | public | AOY Grammy #3 (1973). Tony Visconti producer. Château d'Hérouville. #1 in 14 countries. 21 weeks #1. Multi-Diamond (13x). Queen opened the 1973 tour leg. 1.8B streams. |
| disc_006 | rosie_walker | artist | Concrete & Chrome | Rosie Walker | 1974 | Walker Records | 3 | 1 | Industrial / Krautrock / Berlin | public | AOY Grammy #4 (1975). Brian Eno producer. Hansa Studios Berlin. Commercially underperformed — critics confused. Bowie and Joy Division took notes. Multi-Diamond (4x) retrospectively. |
| disc_007 | rosie_walker | artist | Radio Silence | Rosie Walker | 1977 | Walker Records | 1 | 1 | New Wave / Art Pop | public | AOY Grammy #5 (1978). Homer co-producer. Laurel Canyon. 28 weeks #1 (longest career run). Multi-Diamond (15x). Phoenix (Rise Up) — 3.8B streams / most-licensed song ever recorded. |
| disc_008 | rosie_walker | artist | The Last Cathedral | Rosie Walker | 1979 | Walker Records | 1 | 1 | Cinematic / Orchestral | public | AOY Grammy #6 (1980) — accepted in person: 'Thank you. I'm done.' She meant it. 15 years before the next record. 31 weeks #1 (career peak). Multi-Diamond (10x). Homer engineering. Then The Withdrawal. |

### Full CSV

```csv
id,person_id,credit_type,work_title,artist_name,release_year,label,chart_peak_us,grammy_awards,programme_notes,confidentiality,notes
disc_001,rosie_walker,artist,A Still Small Voice,Rosie Walker,1965,Atlantic Records,12,0,Folk Revival / Chamber Folk / Classical-Inflected Singer-Songwriter,public,Debut album. Greenwich Village. Two weeks recorded. Folk chart #1. Multi-Diamond (3x).
disc_002,rosie_walker,artist,Baptized in Bourbon,Rosie Walker,1968,Atlantic Records,1,0,Muscle Shoals Soul / R&B / Gospel-Rock,public,Transformation record. Wexler + The Swampers. 14 weeks #1. Multi-Diamond (6x). Two consecutive #1 singles (Sunday Clothes / Baptized).
disc_003,rosie_walker,artist,Good Girls Go to Heaven,Rosie Walker,1970,Atlantic Records,1,1,Symphonic Rock / Wall of Sound,public,AOY Grammy #1 (1971). Abbey Road. Quincy Jones producer. Homer Wilson engineer — they met during this session. 22 weeks #1. Multi-Diamond (12x). 2.1B streams on lead single.
disc_004,rosie_walker,artist,Neon Cathedral,Rosie Walker,1971,Atlantic Records,1,1,Art Rock / Psychedelic / Concept Album,public,AOY Grammy #2 (1972). Concept album — religion + technology. Influenced Bowie and punk. 18 weeks #1. Multi-Diamond (11x).
disc_005,rosie_walker,artist,Starlight & Steel,Rosie Walker,1972,Atlantic Records,1,1,Glam Rock / Hard Rock,public,AOY Grammy #3 (1973). Tony Visconti producer. Château d'Hérouville. #1 in 14 countries. 21 weeks #1. Multi-Diamond (13x). Queen opened the 1973 tour leg. 1.8B streams.
disc_006,rosie_walker,artist,Concrete & Chrome,Rosie Walker,1974,Walker Records,3,1,Industrial / Krautrock / Berlin,public,AOY Grammy #4 (1975). Brian Eno producer. Hansa Studios Berlin. Commercially underperformed — critics confused. Bowie and Joy Division took notes. Multi-Diamond (4x) retrospectively.
disc_007,rosie_walker,artist,Radio Silence,Rosie Walker,1977,Walker Records,1,1,New Wave / Art Pop,public,AOY Grammy #5 (1978). Homer co-producer. Laurel Canyon. 28 weeks #1 (longest career run). Multi-Diamond (15x). Phoenix (Rise Up) — 3.8B streams / most-licensed song ever recorded.
disc_008,rosie_walker,artist,The Last Cathedral,Rosie Walker,1979,Walker Records,1,1,Cinematic / Orchestral,public,"AOY Grammy #6 (1980) — accepted in person: 'Thank you. I'm done.' She meant it. 15 years before the next record. 31 weeks #1 (career peak). Multi-Diamond (10x). Homer engineering. Then The Withdrawal."
disc_009,homer_wilson,engineer,Good Girls Go to Heaven,Rosie Walker,1970,Atlantic Records,1,0,Engineering credit — Abbey Road sessions,public,Met Rosie during this session. Told her the mic placement was wrong. She said 'Show me.' They married in 1971.
disc_010,homer_wilson,engineer,Neon Cathedral,Rosie Walker,1971,Atlantic Records,1,0,Engineering credit,public,Second consecutive AOY. Homer and Rosie married this year.
disc_011,homer_wilson,co_producer,Radio Silence,Rosie Walker,1977,Walker Records,1,1,Co-produced with Rosie. Laurel Canyon.,public,Homer's first full co-production credit. The album that earned his studio reputation at the summit of the industry.
disc_012,homer_wilson,engineer,The Last Cathedral,Rosie Walker,1979,Walker Records,1,1,Engineering credit. Co-wrote Homer's Hymn (track 12).,public,Homer's last credit before The Withdrawal. He built the compound studio in the 1980s — it's where every Phase Five record was made.
disc_013,homer_wilson,co_write,Homer's Hymn,Rosie Walker,1979,Walker Records,,0,Track 12 of The Last Cathedral. Love letter in music.,public,The only track explicitly named for him. Simple. Acoustic. Homer's classical ear showing through the orchestration.
disc_014,alex_wilson,artist,Album I — Diventando..,Alex Wilson,2025,Deutsche Grammophon,,,Classical solo piano. Juilliard senior recital programme.,public,Rush release August 22 2025 — 8 days before Grammy eligibility cutoff (Sept 1). Nominated Best Classical Solo Instrumental Album — 68th Grammy Awards (Feb 2 2026). Homer produced at compound studio. Grammy nominations announced Nov 8 2025.
disc_015,alex_wilson,artist,Le Occasioni (Album II),Alex Wilson,TBD,Deutsche Grammophon,,,Schubert Piano Sonata in B-flat major D.960 / Liszt Bénédiction de Dieu dans la solitude / Ravel Gaspard de la nuit / Coda: Montale — from Ti libero la fronte dai ghiaccioli (Le occasioni spoken),confidential,Not yet recorded at story open (January 2026). DG pre-production conversations begun March 2026. Recording begins May 2026 per calendar arc. Homer Wilson producing. Release date TBD — Grammy eligibility question open.
disc_016,rosie_walker,co_write,Chain of Mercy,Aretha Franklin,1967,,1 (R&B),0,,confidential_industry,Full co-write. Originally a folk ballad. Aretha sped it up and made it gospel.
disc_017,rosie_walker,co_write,Suspicious Minds,Elvis Presley,1969,,1,0,,confidential_industry,Wrote the bridge and the iconic fade-out vocal arrangement.
disc_018,rosie_walker,co_write,Rocket Man,Elton John,1972,,2 (UK),0,,confidential_industry,Melody contribution. Elton credits her in his memoir.
disc_019,rosie_walker,co_write,Rebel Rebel,David Bowie,1974,,5 (UK),0,,confidential_industry,Wrote the guitar riff. Gave it to Bowie as a birthday gift.
disc_020,rosie_walker,co_write,The Rose,Bette Midler,1979,,3,0,,confidential_industry,Written by Rosie for Bette. Full songwriting credit under pseudonym.
disc_021,rosie_walker,co_write,Total Eclipse of the Heart,Bonnie Tyler,1983,,1,0,,confidential_industry,Written by Rosie in 1979. Given to Jim Steinman who produced it.
disc_022,rosie_walker,co_write,I Will Survive,Gloria Gaynor,1978,,1,0,,confidential_industry,Wrote the piano intro that defines the song.
disc_023,rosie_walker,session_musician,Dancing Queen,ABBA,1976,,1,0,,confidential_industry,Collaboration during Stockholm sessions. Uncredited. Disputed.
disc_024,rosie_walker,co_write,Heroes,David Bowie,1977,,24 (UK),0,,confidential_industry,Brian Eno confirms Rosie hummed the counter-melody.
disc_025,rosie_walker,co_write,Dreams,Fleetwood Mac,1977,,1,0,,confidential_industry,Sat with Stevie Nicks while she wrote it. Contribution disputed but acknowledged by Nicks.
disc_026,rosie_walker,co_write,9 to 5,Dolly Parton,1980,,1,0,,confidential_industry,Helped create the typewriter percussion rhythm. Dolly's best friend.
disc_027,rosie_walker,artist,Glass Garden,Rosie Walker,1995,Walker Records / UMG (dist.),1,4,"Ambient gospel / early digital textures / analogue warmth fighting machines. Phase Five return.",public,"AOY Grammy #7 (1996). First album in 16 years. No press. No tour. One Walker Records statement. 3M copies week one. Sarah Wilson (Rosie's daughter) is 14 when this drops — Alex not yet born. Tracks: Glass Garden / Root System / Human Frequency / The Shape of Breath / Circuit Hymnal / Soil & Signal / Window Without Sky / The Patient Machine / Harvest Code / Eden in Reverse / The Listening Field / Still It Grows. Singles (all global #1): Glass Garden / Human Frequency / Eden in Reverse. Homer Wilson producing — first collaboration since The Last Cathedral."
disc_028,rosie_walker,artist,A House With No Mirrors,Rosie Walker,2003,Walker Records / UMG (dist.),1,4,"Chamber pop / minimal piano / early 2000s experimental electronica / voice-forward.",public,"AOY Grammy #8 (2004). Recorded 2002–early 2003. Released same year David and Lady Sarah Dawson's son Alex was born; Sarah died in childbirth; Rosie and Homer took Alex home from hospital. Album completed before these events. Walker Records held release briefly. Tracks: A House With No Mirrors / First Light Through Curtains / The Unnamed Room / Skin Without History / Quiet Inheritance / Thread & Bone / Before Language / The Smallest Sound / What We Keep / Echo Without Source / Holding Pattern / Unwritten Ground / Open Door No Witness. Singles (all global #1): A House With No Mirrors / Quiet Inheritance / What We Keep. Homer Wilson producing."
disc_029,rosie_walker,artist,Black Sun Archive,Rosie Walker,2008,Walker Records / UMG (dist.),1,4,"Industrial classical / fractured orchestration / low-end electronics / silence as structure.",public,"AOY Grammy #9 (2009). Released 2008 — year David Wilson (Rosie and Homer's biological son) died of overdose. Alex is 4-5. Not fresh grief — grief of watching a child struggle and lose. Files landed with distributor without prior notice. Not a grief album — a system for storing grief. Tracks: Black Sun Archive / Entry Without Exit / The Last Photograph / Static for the Living / Bone Ledger / Unsent Letters / The Room After / Negative Light / Catalogue of Absence / A Voice in Storage / The Weight of Names / Burn After Listening. Singles (all global #1): Black Sun Archive / The Last Photograph / Catalogue of Absence. Homer Wilson producing."
disc_030,rosie_walker,artist,The Quiet Index,Rosie Walker,2021,Walker Records / UMG (dist.),1,4,"Post-genre minimalism / spatial audio / near-silence / precision composition.",public,"AOY Grammy #10 (2022). Pandemic period. Alex is 17 — finishing Westminster School, preparing for Juilliard. Listened to it alone the night it dropped. Never told anyone what he thought. 40M streams in 72 hours on title track. TikTok ambient content. She did not comment. Tracks: The Quiet Index / Measured Silence / Signal to Dust / The Distance Between Notes / Archive of Air / A World Without Edges / Slow Data / The Final Interval / Everything Still Moving / The Listener Disappears / Index Complete. Singles (all global #1): The Quiet Index / Signal to Dust / Everything Still Moving. Homer Wilson producing."
disc_031,homer_wilson,producer,Glass Garden,Rosie Walker,1995,Walker Records / UMG (dist.),1,0,Producer credit. Phoenix Hollow Studio.,public,Return collaboration with Rosie after 16-year gap. First full production since The Last Cathedral.
disc_032,homer_wilson,producer,A House With No Mirrors,Rosie Walker,2003,Walker Records / UMG (dist.),1,0,Producer credit. Phoenix Hollow Studio.,public,Year Sarah died. Homer and Rosie raising Alex from 2003 onward.
disc_033,homer_wilson,producer,Black Sun Archive,Rosie Walker,2008,Walker Records / UMG (dist.),1,0,Producer credit. Phoenix Hollow Studio.,public,Year David Wilson died. Homer co-raising Alex (then age 4-5).
disc_034,homer_wilson,producer,The Quiet Index,Rosie Walker,2021,Walker Records / UMG (dist.),1,0,Producer credit. Phoenix Hollow Studio.,public,"Alex is 17. Living in Kensington with Rosie and Homer for Westminster. Hears the album drop the same night as everyone else. Tells Homer one sentence the next morning. Homer nods."
disc_035,rosie_walker,co_write,[Post-1995 placements — ongoing],Various artists,1995-2025,Walker Publishing (admin.),,0,Post-1995 ghostwriting and co-write placements. ~2 per year. Selective — artists chosen by Rosie.,confidential_industry,Active placement continues at reduced rate (~2 per year) from 1995 to present. Specific placements to be added to this file as story requires. All administered by Walker Publishing.
```

---

## Source: `data_media_coverage_timeline.csv` {#data-media-coverage-timeline-csv}

### Columns

| Column |
|---|
| `id` |
| `date` |
| `outlet` |
| `outlet_tier` |
| `headline_or_description` |
| `coverage_type` |
| `public_knowledge` |
| `tabloid_source` |
| `information_ceiling` |
| `verification_status` |
| `notes` |

### Preview

| id | date | outlet | outlet_tier | headline_or_description | coverage_type | public_knowledge | tabloid_source | information_ceiling | verification_status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| media_001 | 2025-05-22 | multiple_outlets | broadsheet+tabloid | Juilliard commencement video — Alex Wilson crossing the stage; 12M views in 4 days | viral_social | true | multiple | public_performance_only | verified | The clip that started everything. The Ravel senior recital footage embedded. Dr. Marlowe quote confirmed. Classical press follows 2 weeks later. |
| media_002 | 2025-05-25 | New York Times (Arts) | classical_press | Review: Juilliard Senior Recital — 'A Debut by Any Other Name' | review | true |  | performance_and_musical_history | verified | First serious classical press. Sets the tone — this is not a celebrity album story. Musical language throughout. |
| media_003 | 2025-06-01 | DeuxMoi | gossip_digital | Blind item: young classical musician signed major deal — 'who is this?' | blind_item | false | deuxmoi | industry_speculation_only | unverified | Pre-announcement speculation. Circulates in gossip ecosystem without confirmation. Correctly identified but not named. |
| media_004 | 2025-07-01 | Page Six | tabloid_us | First appearance in celeb tabloid context — spotted at event summer circuit; brief item | spotted | true | page_six | public_appearance_only | verified | First time he appears in Page Six. Brief item. No detail. Just presence noted at a summer event. |
| media_005 | 2025-07-08 | Daily Mail | tabloid_uk | EXCLUSIVE: Classical heir and supermodel — Vittoria Ceretti photographed together in Sardinia | confirmed_hookup | true | daily_mail | confirmed_photo_proximity | verified_photo | The Ceretti story. Daily Mail had a photograph — unambiguous. He didn't comment. Story ran 72 hours in tabloid cycle. |
| media_006 | 2025-07-15 | multiple_outlets | tabloid+celebrity | Ceretti story follow-up cycle — fan account aggregation; relationship speculation | follow_up | true | multiple | public_photo_only | verified_reputable | Standard follow-up cycle. No new information — fan accounts doing aggregation and speculation based on the Daily Mail photo. |
| media_007 | 2025-08-01 | DeuxMoi | gossip_digital | Blind: 'Dove Cameron in London with major classical talent — very cozy' | strongly_suspected | false | deuxmoi | speculation_only | unverified | The Dove Cameron rumour. DeuxMoi blind. Circulates in gossip-aware social media. Not confirmed. Strongly_suspected per canon. |
| media_008 | 2025-08-22 | Deutsche Grammophon (press release) | industry_trade | ALBUM RELEASE: Alex Wilson — Album I — Diventando.. — Deutsche Grammophon debut | release_announcement | true |  | release_date_and_programme | verified | Rush release. DG press release coordinated with Askonas Holt. NPR Music + classical press review copies sent day of. Standard DG release infrastructure. |

### Full CSV

```csv
id,date,outlet,outlet_tier,headline_or_description,coverage_type,public_knowledge,tabloid_source,information_ceiling,verification_status,notes
media_001,2025-05-22,multiple_outlets,broadsheet+tabloid,Juilliard commencement video — Alex Wilson crossing the stage; 12M views in 4 days,viral_social,true,multiple,public_performance_only,verified,The clip that started everything. The Ravel senior recital footage embedded. Dr. Marlowe quote confirmed. Classical press follows 2 weeks later.
media_002,2025-05-25,New York Times (Arts),classical_press,Review: Juilliard Senior Recital — 'A Debut by Any Other Name',review,true,,performance_and_musical_history,verified,First serious classical press. Sets the tone — this is not a celebrity album story. Musical language throughout.
media_003,2025-06-01,DeuxMoi,gossip_digital,Blind item: young classical musician signed major deal — 'who is this?',blind_item,false,deuxmoi,industry_speculation_only,unverified,Pre-announcement speculation. Circulates in gossip ecosystem without confirmation. Correctly identified but not named.
media_004,2025-07-01,Page Six,tabloid_us,First appearance in celeb tabloid context — spotted at event summer circuit; brief item,spotted,true,page_six,public_appearance_only,verified,First time he appears in Page Six. Brief item. No detail. Just presence noted at a summer event.
media_005,2025-07-08,Daily Mail,tabloid_uk,EXCLUSIVE: Classical heir and supermodel — Vittoria Ceretti photographed together in Sardinia,confirmed_hookup,true,daily_mail,confirmed_photo_proximity,verified_photo,The Ceretti story. Daily Mail had a photograph — unambiguous. He didn't comment. Story ran 72 hours in tabloid cycle.
media_006,2025-07-15,multiple_outlets,tabloid+celebrity,Ceretti story follow-up cycle — fan account aggregation; relationship speculation,follow_up,true,multiple,public_photo_only,verified_reputable,Standard follow-up cycle. No new information — fan accounts doing aggregation and speculation based on the Daily Mail photo.
media_007,2025-08-01,DeuxMoi,gossip_digital,Blind: 'Dove Cameron in London with major classical talent — very cozy',strongly_suspected,false,deuxmoi,speculation_only,unverified,The Dove Cameron rumour. DeuxMoi blind. Circulates in gossip-aware social media. Not confirmed. Strongly_suspected per canon.
media_008,2025-08-22,Deutsche Grammophon (press release),industry_trade,ALBUM RELEASE: Alex Wilson — Album I — Diventando.. — Deutsche Grammophon debut,release_announcement,true,,release_date_and_programme,verified,Rush release. DG press release coordinated with Askonas Holt. NPR Music + classical press review copies sent day of. Standard DG release infrastructure.
media_009,2025-08-28,Gramophone,classical_press,Editor's Choice: 'Alex Wilson — Diventando.. — An astonishing debut',review,true,,musical_content_and_biography,verified,First major classical press review. Editor's Choice. Sets classical credibility before broader press arrives.
media_010,2025-09-01,Vogue (US),fashion_press,September cover: 'The Classical Kid' — Alex Wilson — full interview and shoot,cover_feature,true,,public_biography_and_artistic_history,verified,Shot in late July. Anna's team styled. Interview focused on Homer and recording process rather than fame. Published version has traces of that. The cover image reframes his public identity.
media_011,2025-09-01,Pitchfork Classical,music_press,Review: 8.4 — 'Alex Wilson — Diventando..' — 'Three paragraphs on the Ravel',review,true,,musical_analysis,verified,8.4 from Pitchfork Classical is a significant score. Three paragraphs on the Ravel. Sets the non-celebrity music-press narrative.
media_012,2025-09-10,New York Times (Arts),broadsheet,Full review: 'Alex Wilson's Debut Is Not What Anyone Expected — And That's the Point',review,true,,musical_content_and_public_artistic_biography,verified,NYT review. Positive. Comparative context — classical debut treated as serious music event not celebrity crossover.
media_013,2025-09-15,multiple_outlets,tabloid+celebrity,Fashion house signing announcement wave — Versace / Stella McCartney / Dior / Loewe announced in coordination pre-NYFW,deal_announcement,true,,deal_existence_and_brand_names,verified,James Latham coordinated announcement timing with fashion week calendar. Four houses announced in two weeks. Press explosion — cultural reframing begins.
media_014,2025-09-22,DeuxMoi,gossip_digital,Blind: 'Hunter Schafer and classical musician — Paris Fashion Week — hotel corridor situation',strongly_suspected,false,deuxmoi,speculation_only,unverified,The Hunter Schafer story. Paris FW context. DeuxMoi blind. Circulates in fan account ecosystem. Not confirmed. Strongly_suspected per canon.
media_015,2025-09-25,WWD,fashion_trade,Front row breakdown — Paris Fashion Week — Alex Wilson attends 4 shows in 3 days,front_row,true,,attendance_and_brand_affiliations,verified,Fashion trade coverage. Professional. Front row logistics and brand affiliations noted accurately.
media_016,2025-10-01,DeuxMoi,gossip_digital,Blind: 'Addison Rae and classical heir — after-hours Paris FW — 'confirmed by multiple sources',strongly_suspected,false,deuxmoi,speculation_only,unverified,The Addison Rae story. Paris FW first week October. DeuxMoi. Strongly_suspected per canon. Multiple-source language in the blind.
media_017,2025-10-17,Page Six,tabloid_us,PHOTO: Alex Wilson + Taylor Russell — post-Carnegie Hall — Tribeca after-party — 'very close all night',one_photo,true,page_six,public_appearance_proximity,verified_photo,The Taylor Russell story. Page Six ran the morning after Carnegie Hall. One frame. Unambiguous proximity. No context. Classic one-photo tabloid item.
media_018,2025-10-18,multiple_outlets,tabloid+celebrity,Russell follow-up cycle — fan speculation; no new information,follow_up,true,multiple,public_photo_only,unverified_rumour,Standard cycle. Page Six photo drives 24 hours of fan account posts and celebrity gossip site items. Nothing confirmed.
media_019,2025-10-20,multiple_outlets,classical_press,Post-Carnegie Hall reviews — 'best solo debut at Carnegie in a decade',review,true,,performance_and_programme,verified,Multiple classical outlets. Consensus: serious debut. The performance separated from the celebrity context deliberately — classical press resists the tabloid framing.
media_020,2025-11-01,Burberry (announcement),fashion_press,Burberry signs Alex Wilson — deal announced; campaign images not yet released,deal_announcement,true,,deal_existence,verified,Fifth fashion house. Announcement only — no campaign imagery. Images will follow campaign shoot (April 2026).
media_021,2025-11-08,Recording Academy (official),music_industry,68th Grammy Nominations announced — Alex Wilson nominated Best Classical Solo Instrumental Album (Diventando..),nomination_announcement,true,,nomination_category_and_album,verified,Official Recording Academy announcement. Covered by Billboard / Rolling Stone / classical press. DG put out a press release. He was at the compound when it came through.
media_022,2025-11-09,multiple_outlets,music_press+broadsheet,Grammy nomination follow-up — classical breakthrough narrative; 'youngest nominee in category in 15 years',nomination_coverage,true,,nomination_plus_biographical_context,verified,Standard follow-up cycle. Classical press + music trades. Age angle noted. 'Youngest nominee in category' framing runs across multiple outlets.
media_023,2025-11-15,GQ (US),men_interest,Cover and 8-page spread confirmed for January 2026 issue — shoot November 2025,forthcoming_preview,true,,forthcoming_shoot_confirmed,verified,GQ cover shot November 2025. Published January 17 2026. Preview item in November confirms it's coming.
media_024,2025-12-05,multiple_outlets,classical_press,Wigmore Hall London — 'second major recital in three months — the classical world paying attention differently now',review,true,,performance_and_programme,verified,Wigmore Hall. London. Second recital after Carnegie. Classical press tone shifts — from debut curiosity to established presence. Different weight now.
media_025,2025-12-10,multiple_outlets,fashion+broadsheet,Met Gala co-chair announcement — December 10 2025 for May 2026 ceremony — Young Met Board connection noted,announcement,true,,co_chair_status_and_young_met_board,verified,Eleanor managed announcement timing. Fashion press + broadsheet arts coverage. Co-chair confirms cultural ambition at the intersection of music and fashion.
media_026,2026-01-17,GQ (US),men_interest,GQ cover published — 'The Classical Kid Arrives' — 8-page spread; interview from November 2025,cover_feature,true,,public_biography_and_artistic_history,verified,The GQ cover that opens the story week. He's read it. Elton texts immediately. He doesn't recognise himself entirely but it isn't wrong.
media_027,2026-01-20,multiple_outlets,music_press,Grammy nominee spotlight — Recording Academy media week begins; press commitments,nominee_feature,true,,nomination_and_album_content,verified,Grammy week press commitments. Nadia coordinates. Two days of press interviews.
media_028,2026-02-02,broadcast+live,grammy_broadcast,68th Grammy Awards ceremony — Best Classical Solo Instrumental Album category result,grammy_ceremony,true,,ceremony_result_public,pending,OUTCOME TBD — Ryan story arc decision. Grammy ceremony broadcast globally. Classical category results widely covered regardless of outcome.
```

---

## Source: `data_wilson_hookup_tracker.csv` {#data-wilson-hookup-tracker-csv}

### Columns

| Column |
|---|
| `id` |
| `person_id` |
| `date_range` |
| `location_id` |
| `confidence_level` |
| `primary_source` |
| `source_tier` |
| `follow_up_coverage` |
| `public_knowledge` |
| `details_public` |
| `details_private` |
| `flair_note` |

### Preview

| id | person_id | date_range | location_id | confidence_level | primary_source | source_tier | follow_up_coverage | public_knowledge | details_public | details_private | flair_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hookup_001 | vittoria_ceretti | 2025-07-08 to 2025-07-22 | villa_serena | confirmed | daily_mail | tier1_tabloid_uk | Follow-up cycle 72 hours: multiple tabloid reprints, fan account aggregation, Instagram activity analysis | true | Daily Mail had photograph. Unambiguous proximity. Sardinia location confirmed. No context. No statement from either party. | They were in Sardinia for three weeks. La Terrazza crew present. Vittoria arrived as a guest of the summer circuit, not as Alex's guest specifically. The photograph happened on the third day. He didn't find out the Mail had it until Kevin mentioned it. | Tommaso found the situation extremely funny. Said so, repeatedly. Vittoria was unfazed. Alex was annoyed about the photograph for approximately 48 hours and then moved on. |
| hookup_002 | alix_earle | 2025-07-01 | ibiza | rumour | deuxmoi | tier2_gossip_digital | Single DeuxMoi blind. Did not circulate significantly. 24-hour shelf life. | false | DeuxMoi blind item only. No photo. No named source. Described as 'brief encounter' by the blind's phrasing. | Brief. Ibiza context. Nothing that required conversation or management. | The Ibiza one. File and forget. Even DeuxMoi wasn't sure. |
| hookup_003 | dove_cameron | 2025-08-20 | kensington_london | strongly_suspected | deuxmoi | tier2_gossip_digital | Single blind. Some fan account reposting. 48-hour cycle. | false | DeuxMoi blind: 'major classical talent + Dove Cameron — very cozy in London.' No photo. No location specificity. | London. Kensington. August. The blind is accurate in its impression if not its detail. | The one where the blind writer clearly had secondhand information and was guessing at the geometry. Still got the basic facts right. |
| hookup_004 | hunter_schafer | 2025-09-22 | paris | strongly_suspected | deuxmoi | tier2_gossip_digital | Multiple reposts. Fashion week amplification — gossip-aware fashion audience. 72-hour cycle. | false | DeuxMoi blind: 'Hunter Schafer and classical musician — Paris Fashion Week — hotel corridor situation.' Multiple-source language in the blind. | Paris Fashion Week. The blind is more specific than the Ibiza or London ones. Hotel corridor is a specific detail that suggests someone was there. | Fashion week is a small world. The blind writer almost certainly got this from someone adjacent to the event. The 'hotel corridor' detail is specific enough to be real. |
| hookup_005 | addison_rae | 2025-10-01 | paris | strongly_suspected | deuxmoi | tier2_gossip_digital | Multiple reposts. DeuxMoi followed up 24 hours later with 'multiple sources now confirming.' | false | DeuxMoi blind with follow-up: 'Addison Rae and classical heir — after-hours Paris FW.' Followed by 'multiple sources confirming' post. | Paris Fashion Week first week October. Different event from Hunter Schafer (different week). The 'multiple sources' follow-up is unusual for DeuxMoi — suggests multiple people saw something. | The DeuxMoi follow-up is rarer than the initial blind and suggests genuine information reach. Nothing confirmed officially. Addison's team did not comment. |
| hookup_006 | taylor_russell | 2025-10-17 | carnegie_hall | one_photo | page_six | tier1_tabloid_us | 24-hour cycle: celebrity gossip sites reprint the Page Six photo; fan account speculation; no new information beyond the photo. | true | Page Six ran the morning after Carnegie Hall. One frame. Unambiguous proximity at the Tribeca after-party. No statement from either party. | Carnegie Hall October 17. After-party Tribeca. Taylor Russell was at the show — she has a documented interest in classical music. The photograph was taken at the after-party, not the concert. | He saw it before Kevin mentioned it. Put his phone in his pocket. Nadia had fielded three press enquiries by the time he woke up the next morning. |
| hookup_007 | olivia_rodrigo | 2025-06-27 to 2025-06-29 | glastonbury | strongly_suspected | deuxmoi | tier2_gossip_digital | Multiple reposts across r/AlexWilson and Olivia Rodrigo fan accounts. 72-hour cycle. Both fan communities briefly feral. Died down when no photo emerged. | false | DeuxMoi blind: 'Classical heir and major pop artist — Glastonbury weekend — very close energy, multiple people saw them together.' Fan accounts cross-referenced both their whereabouts in the VIP field on the same evening. No statement from either party. | Glastonbury. Both on the VIP circuit. Their paths crossed in the hospitality area, not the crowd. Camille saw it and said nothing for three days. Tommy was also at Glastonbury and has opinions he has kept exclusively to himself. | The one where the age match (both born 2003) sent the internet briefly feral. Classical music press: zero coverage. Pop press: 48 hours of 'are they??' then silence when no photo landed. |

### Full CSV

```csv
id,person_id,date_range,location_id,confidence_level,primary_source,source_tier,follow_up_coverage,public_knowledge,details_public,details_private,flair_note
hookup_001,vittoria_ceretti,2025-07-08 to 2025-07-22,villa_serena,confirmed,daily_mail,tier1_tabloid_uk,"Follow-up cycle 72 hours: multiple tabloid reprints, fan account aggregation, Instagram activity analysis","true","Daily Mail had photograph. Unambiguous proximity. Sardinia location confirmed. No context. No statement from either party.","They were in Sardinia for three weeks. La Terrazza crew present. Vittoria arrived as a guest of the summer circuit, not as Alex's guest specifically. The photograph happened on the third day. He didn't find out the Mail had it until Kevin mentioned it.","Tommaso found the situation extremely funny. Said so, repeatedly. Vittoria was unfazed. Alex was annoyed about the photograph for approximately 48 hours and then moved on."
hookup_002,alix_earle,2025-07-01,ibiza,rumour,deuxmoi,tier2_gossip_digital,"Single DeuxMoi blind. Did not circulate significantly. 24-hour shelf life.","false","DeuxMoi blind item only. No photo. No named source. Described as 'brief encounter' by the blind's phrasing.","Brief. Ibiza context. Nothing that required conversation or management.","The Ibiza one. File and forget. Even DeuxMoi wasn't sure."
hookup_003,dove_cameron,2025-08-20,kensington_london,strongly_suspected,deuxmoi,tier2_gossip_digital,"Single blind. Some fan account reposting. 48-hour cycle.","false","DeuxMoi blind: 'major classical talent + Dove Cameron — very cozy in London.' No photo. No location specificity.","London. Kensington. August. The blind is accurate in its impression if not its detail.","The one where the blind writer clearly had secondhand information and was guessing at the geometry. Still got the basic facts right."
hookup_004,hunter_schafer,2025-09-22,paris,strongly_suspected,deuxmoi,tier2_gossip_digital,"Multiple reposts. Fashion week amplification — gossip-aware fashion audience. 72-hour cycle.","false","DeuxMoi blind: 'Hunter Schafer and classical musician — Paris Fashion Week — hotel corridor situation.' Multiple-source language in the blind.","Paris Fashion Week. The blind is more specific than the Ibiza or London ones. Hotel corridor is a specific detail that suggests someone was there.","Fashion week is a small world. The blind writer almost certainly got this from someone adjacent to the event. The 'hotel corridor' detail is specific enough to be real."
hookup_005,addison_rae,2025-10-01,paris,strongly_suspected,deuxmoi,tier2_gossip_digital,"Multiple reposts. DeuxMoi followed up 24 hours later with 'multiple sources now confirming.'","false","DeuxMoi blind with follow-up: 'Addison Rae and classical heir — after-hours Paris FW.' Followed by 'multiple sources confirming' post.","Paris Fashion Week first week October. Different event from Hunter Schafer (different week). The 'multiple sources' follow-up is unusual for DeuxMoi — suggests multiple people saw something.","The DeuxMoi follow-up is rarer than the initial blind and suggests genuine information reach. Nothing confirmed officially. Addison's team did not comment."
hookup_006,taylor_russell,2025-10-17,carnegie_hall,one_photo,page_six,tier1_tabloid_us,"24-hour cycle: celebrity gossip sites reprint the Page Six photo; fan account speculation; no new information beyond the photo.","true","Page Six ran the morning after Carnegie Hall. One frame. Unambiguous proximity at the Tribeca after-party. No statement from either party.","Carnegie Hall October 17. After-party Tribeca. Taylor Russell was at the show — she has a documented interest in classical music. The photograph was taken at the after-party, not the concert.","He saw it before Kevin mentioned it. Put his phone in his pocket. Nadia had fielded three press enquiries by the time he woke up the next morning."
hookup_007,olivia_rodrigo,2025-06-27 to 2025-06-29,glastonbury,strongly_suspected,deuxmoi,tier2_gossip_digital,"Multiple reposts across r/AlexWilson and Olivia Rodrigo fan accounts. 72-hour cycle. Both fan communities briefly feral. Died down when no photo emerged.","false","DeuxMoi blind: 'Classical heir and major pop artist — Glastonbury weekend — very close energy, multiple people saw them together.' Fan accounts cross-referenced both their whereabouts in the VIP field on the same evening. No statement from either party.","Glastonbury. Both on the VIP circuit. Their paths crossed in the hospitality area, not the crowd. Camille saw it and said nothing for three days. Tommy was also at Glastonbury and has opinions he has kept exclusively to himself.","The one where the age match (both born 2003) sent the internet briefly feral. Classical music press: zero coverage. Pop press: 48 hours of 'are they??' then silence when no photo landed."
```

---

## Source: `archive_FORWARD_STATE.md` {#archive-forward-state-md}

# FORWARD STATE — POST-FRESH_KY CANON PARKING LOT
file_id: forward_state
canonical_reference: CORRECTIONS.md C43, C44, C45, C47, C50

> **⚠️ READ THIS FIRST.** FRESH_KY timeline is **early June 2025** (~5–7 days after Juilliard graduation May 22). The items below are canon from later sessions that ran ahead of that story date. They describe events and relationships that happen MONTHS or YEARS after story-present.
>
> **Do not apply these items to FRESH_KY scenes.** They are parked here so that (a) they aren't lost, and (b) when the timeline reaches them, future Claudes know the canon decisions that have already been made.
>
> If a scene is set after the relevant trigger date, this file becomes live. Until then, these items are inert.

---

## LATER-STORY CANON — APPLY WHEN TIMELINE REACHES

### Clara — BBC / Wogan House (London)
**Not active in FRESH_KY.** Per C44, Clara is in **London at Wogan House** (BBC Radio). She is not flying to NYC for any first voice moment. Future scenes involving Clara take place in London, BBC radio infrastructure. Clara is the interviewer/broadcaster who becomes the first significant public voice moment for Alex post-Rule.

**Trigger:** Post-late-June 2025, once AL.X has cleared inbound and The Lede has mapped the first public-voice outlets.

### Olivia Rodrigo — industry-adjacent, not press-calendar-aware
**Not active in FRESH_KY.** Per C43, Olivia is an industry-adjacent figure in Alex's circle (Summer House / crossover). She does **not** know Alex's press calendar, does **not** know specifically when Clara's interview drops, does **not** have insider access to Alex's private scheduling. Future scenes should write her as a peer who reads the news like everyone else — warmly, as a friend, but without operational knowledge.

**Canon lock:** Do not drift between "Liv Rodrigo" and "Olivia Rodrigo" — the canonical form is Olivia (C49).

### Chiara at Via Carota (NYC dinner beat)
**Not active in FRESH_KY.** Per C45, a specific future dinner scene at Via Carota (West Village, NYC) features Chiara — and her "composure issue" at that scene is **anticipation**, not surprise. She already knew Alex was coming. Do not write her as discovering his presence. She was expecting him and was nervous ahead of the meeting.

**Trigger:** Whenever the Via Carota scene is opened. Likely later 2025 or 2026.

### Milan men's-week / Versace windows
**Not active in FRESH_KY.** Per C17 and C47, **Milan men's week on Solstice weekend is dead** — Nella/Donatella would never ask Alex to skip Solstice. Any Versace-men's-week scene must use a later window (not June). Use the September or January men's windows instead. Nella knows Solstice holds; this is not a scheduling conflict that would be proposed.

**Trigger:** Whenever Milan fashion-week beats come into play (September 2025 men's window is the first plausible Versace moment).

### Henry Cabot — NYL infrastructure, not Alex's producer
**Not active in FRESH_KY in the wrong direction.** Per C50, Henry Cabot is **NYL infrastructure energy** — an existing member of the New York Lot, Alex's cohort. He is not moving cars, tables, or operational pieces for Alex unless explicitly stated. He is not Alex's producer. Do not promote him into an operational role.

**Current canon:** Henry is a friend and cohort member. Bar-side, dinner-side, party-side — yes. Operations-side — no.

---

## NARRATOR USE

- **In FRESH_KY (May 29, 2025 – early June 2025):** this file is effectively inert. None of the above are live.
- **In later timelines:** consult this file to avoid re-inventing canon that's already been decided. These items are locked regardless of when the scene is written.
- **If a session is set between FRESH_KY's current state and these triggers:** the items are still inert. Do not pull them forward.
- **Never introduce these items to a FRESH_KY scene as "news."** Clara is not yet on the horizon. Via Carota with Chiara hasn't been scheduled. Versace men's week is months away. Henry has not been pitched to Alex as anything operational.

---

## REGISTER CALIBRATION — APPLIES TO ANY TIMELINE

These items from CORRECTIONS.md are register-level rules, not timeline-specific. They apply whenever relevant.

### C42 — Cheeky register when Ryan steers cheeky
When Ryan steers Alex toward playful, cheeky, TikTok-live, good-light-TV, or Chicken-Shop-Date register, **stop building prestige ramps**. The register is Clara-in-jeans, not Vogue-cover. Alex killed the "first sentence" prestige campaign himself. When the direction is cheeky, write cheeky.

### C48 — Alex's number is secure
No unknown-number missed calls. No cold-call beats. Greystone runs 24/7 threat monitoring; only saved contacts ring through. See FM-21.

### C52 — Family chat rhythm
Assume Alex has already replied to Rosie, Homer, and Apple in ordinary family rhythm. Do not waste phone renders on routine family check-ins. Render family when something specific is happening, not as ambient texture.

---

## CROSS-REFERENCES
- `01_RUNTIME_RULES.md §C17, C43, C44, C45, C46, C47, C48, C49, C50, C52` — source
- `08_TIMELINE_AND_FORWARD_STATE.md` — timeline anchor
- `06_PUBLIC_LAYER_AND_MUSIC.md §STORY DATE` — FRESH_KY entry point
