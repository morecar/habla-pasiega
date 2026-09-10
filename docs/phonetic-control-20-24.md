# Control de transcripción fonética: §§ 20–24

Tabla regenerable para cotejar cada forma dialectal. La columna «lectura RFE» es una transliteración Unicode de control; el PDF conserva los glifos de Penny.

## Inventario componible

| Macro | Rasgo conservado |
|---|---|
| `\rfeStress{x}` | acento de intensidad sobre la vocal |
| `\rfeLong` | cantidad larga, independiente del acento |
| `\rfeMixedI`, `\rfeMixedU` | vocales mixtas o engoladas |
| `\rfePalatalA` | *a* palatal especial |
| `\rfeStressedMixedI`, `\rfeStressedMixedU` | vocal mixta tónica |
| `\rfeRelaxedPalatal` | vocal final relajada palatal |
| `\rfeRelaxedClosed` | vocal final relajada muy cerrada |
| `\rfeVeryPalatal` | variante final muy palatal |

## Formas etiquetadas

| § | Original de Penny (lectura de control) | Unicode buscable | Código TeX | Resultado PDF |
|---:|---|---|---|---|
| 21 bis | `indrǘsku` | `indruscu` | `\dialectform{indruscu}{indr\rfeStressedMixedU sku}` | compilación 44, p. 37 |
| 21 bis | `andrwḯski` | `andruisqui` | `\dialectform{andruisqui}{andrw\rfeStressedMixedI ski}` | compilación 44, p. 37 |
| 21 bis | `isklǘjü` | `iscluiu` | `\dialectform{iscluiu}{iskl\rfeStressedMixedU j\rfeMixedU}` | compilación 44, p. 37 |
| 21 bis | `iskwḯdü` | `iscluidu` | `\dialectform{iscluidu}{iskw\rfeStressedMixedI d\rfeMixedU}` | compilación 44, p. 37 |
| 21 bis | `pidigwḯnü` | `pidigüinu` | `\dialectform{pidigüinu}{pidigw\rfeStressedMixedI n\rfeMixedU}` | compilación 44, p. 37 |
| 21 bis | `kǘrpunü` | `curpuñu` | `\dialectform{curpuñu}{k\rfeStressedMixedU rpun\rfeMixedU}` | compilación 44, p. 37 |
| 21 bis | `lubjḯsü` | `lubjisu` | `\dialectform{lubjisu}{lubj\rfeStressedMixedI s\rfeMixedU}` | compilación 44, p. 37 |
| 22 | `prepará:` | `preparái` | `\dialectform{preparái}{prepar\rfeStress{a}\rfeLong}` | compilación 44, p. 37 |
| 22 | `išá:` | `ixái` | `\dialectform{ixái}{iS\rfeStress{a}\rfeLong}` | compilación 44, p. 37 |
| 22 | `tostá:s` | `tostáis` | `\dialectform{tostáis}{tost\rfeStress{a}\rfeLong s}` | compilación 44, p. 37 |
| 22 | `mereθí:s` | `merecís` | `\dialectform{merecís}{mereT\rfeStress{i}\rfeLong s}` | compilación 44, p. 37 |
| 22 | `agraiθí:s` | `agraicís` | `\dialectform{agraicís}{agraiT\rfeStress{i}\rfeLong s}` | compilación 44, p. 37 |
| 22 | `salí:s` | `salís` | `\dialectform{salís}{sal\rfeStress{i}\rfeLong s}` | compilación 44, p. 37 |
| 22 | `midí:s` | `midís` | `\dialectform{midís}{mid\rfeStress{i}\rfeLong s}` | compilación 44, p. 37 |
| 22 | `gulbí:` | `gulbí` | `\dialectform{gulbí}{gulb\rfeStress{i}\rfeLong}` | compilación 44, p. 37 |
| 22 | `kumí:` | `cumí` | `\dialectform{cumí}{kum\rfeStress{i}\rfeLong}` | compilación 44, p. 37 |
| 22 | `biní:` | `biní` | `\dialectform{biní}{bin\rfeStress{i}\rfeLong}` | compilación 44, p. 37 |
| 22 | `kají:stẹs` | `cayístis` | `\dialectform{cayístis}{kaj\rfeStress{i}\rfeLong st\rfeRelaxedClosed s}` | compilación 44, p. 37 |
| 22 | `iθí:stẹs` | `icístis` | `\dialectform{icístis}{iT\rfeStress{i}\rfeLong st\rfeRelaxedClosed s}` | compilación 44, p. 37 |
| 22 | `istubí:stẹs` | `istubístis` | `\dialectform{istubístis}{istub\rfeStress{i}\rfeLong st\rfeRelaxedClosed s}` | compilación 44, p. 37 |
| 22 | `móstru:` | `mostru` | `\dialectform{mostru}{m\rfeStress{o}stru\rfeLong}` | compilación 44, p. 37 |
| 23 | `kárę` | `care` | `\dialectform{care}{k\rfeStress{a}r\rfeRelaxedPalatal}` | compilación 44, p. 37-38 |
| 23 | `mirjéndę` | `mirjende` | `\dialectform{mirjende}{mirj\rfeStress{e}nd\rfeRelaxedPalatal}` | compilación 44, p. 37-38 |
| 23 | `gwénę` | `güene` | `\dialectform{güene}{gw\rfeStress{e}n\rfeRelaxedPalatal}` | compilación 44, p. 37-38 |
| 23 | `négrę` | `negre` | `\dialectform{negre}{n\rfeStress{e}gr\rfeRelaxedPalatal}` | compilación 44, p. 37-38 |
| 23 | `áblę` | `able` | `\dialectform{able}{\rfeStress{a}bl\rfeRelaxedPalatal}` | compilación 44, p. 37-38 |
| 23 | `póŋgę` | `ponge` | `\dialectform{ponge}{p\rfeStress{o}Ng\rfeRelaxedPalatal}` | compilación 44, p. 37-38 |
| 23 | `gwénęs` | `güenes` | `\dialectform{güenes}{gw\rfeStress{e}n\rfeRelaxedPalatal s}` | compilación 44, p. 37-38 |
| 23 | `négręs` | `negres` | `\dialectform{negres}{n\rfeStress{e}gr\rfeRelaxedPalatal s}` | compilación 44, p. 37-38 |
| 23 | `áblęs` | `ables` | `\dialectform{ables}{\rfeStress{a}bl\rfeRelaxedPalatal s}` | compilación 44, p. 37-38 |
| 23 | `póŋgęn` | `pongen` | `\dialectform{pongen}{p\rfeStress{o}Ng\rfeRelaxedPalatal n}` | compilación 44, p. 37-38 |
| 23 | `grándẹ` | `grandi` | `\dialectform{grandi}{gr\rfeStress{a}nd\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `dálẹ` | `dali` | `\dialectform{dali}{d\rfeStress{a}l\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `réẹ` | `re` | `\dialectform{re}{r\rfeStress{e}\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `tárdẹ` | `tardi` | `\dialectform{tardi}{t\rfeStress{a}rd\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `sálẹ` | `sali` | `\dialectform{sali}{s\rfeStress{a}l\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `kómẹ` | `comi` | `\dialectform{comi}{k\rfeStress{o}m\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `intrjégẹ` | `intrjegi` | `\dialectform{intrjegi}{intrj\rfeStress{e}g\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `bíbẹ` | `bibi` | `\dialectform{bibi}{b\rfeStress{i}b\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `kúrẹ` | `curri` | `\dialectform{curri}{k\rfeStress{u}r\rfeRelaxedClosed}` | compilación 44, p. 37-38 |
| 23 | `grándẹs` | `grandis` | `\dialectform{grandis}{gr\rfeStress{a}nd\rfeRelaxedClosed s}` | compilación 44, p. 37-38 |
| 23 | `dálẹs` | `dalis` | `\dialectform{dalis}{d\rfeStress{a}l\rfeRelaxedClosed s}` | compilación 44, p. 37-38 |
| 23 | `tárdẹs` | `tardis` | `\dialectform{tardis}{t\rfeStress{a}rd\rfeRelaxedClosed s}` | compilación 44, p. 37-38 |
| 23 | `sálẹs` | `salis` | `\dialectform{salis}{s\rfeStress{a}l\rfeRelaxedClosed s}` | compilación 44, p. 37-38 |
| 23 | `kómẹs` | `comis` | `\dialectform{comis}{k\rfeStress{o}m\rfeRelaxedClosed s}` | compilación 44, p. 37-38 |
| 23 | `intrjégẹn` | `intrjegin` | `\dialectform{intrjegin}{intrj\rfeStress{e}g\rfeRelaxedClosed n}` | compilación 44, p. 37-38 |
| 23 | `málus` | `malus` | `\dialectform{malus}{m\rfeStress{a}lus}` | compilación 44, p. 37-38 |
| 23 | `mánus` | `manus` | `\dialectform{manus}{m\rfeStress{a}nus}` | compilación 44, p. 37-38 |
| 23 | `kwérnus` | `cuernus` | `\dialectform{cuernus}{kw\rfeStress{e}rnus}` | compilación 44, p. 37-38 |
| 23 | `éstu` | `estu` | `\dialectform{estu}{\rfeStress{e}stu}` | compilación 44, p. 37-38 |
| 23 | `ésto` | `esto` | `\dialectform{esto}{\rfeStress{e}sto}` | compilación 44, p. 37-38 |
| 23 | `ísti késu és` | `isti quesu es` | `\dialectform{isti quesu es}{\rfeStress{i}sti k\rfeStress{e}su
\rfeStress{e}s}` | compilación 44, p. 37-38 |
| 23 | `gwénu` | `güenu` | `\dialectform{güenu}{gw\rfeStress{e}nu}` | compilación 44, p. 37-38 |
| 23 | `gwéno` | `güeno` | `\dialectform{güeno}{gw\rfeStress{e}no}` | compilación 44, p. 37-38 |
| 23 | `sálgu` | `salgu` | `\dialectform{salgu}{s\rfeStress{a}lgu}` | compilación 44, p. 37-38 |
| 23 | `sálgo` | `salgo` | `\dialectform{salgo}{s\rfeStress{a}lgo}` | compilación 44, p. 37-38 |
| 23 | `kántu` | `cantu` | `\dialectform{cantu}{k\rfeStress{a}ntu}` | compilación 44, p. 37-38 |
| 23 | `kánto` | `canto` | `\dialectform{canto}{k\rfeStress{a}nto}` | compilación 44, p. 37-38 |
| 23 | `košémus` | `coxemus` | `\dialectform{coxemus}{koS\rfeStress{e}mus}` | compilación 44, p. 37-38 |
| 23 | `salémus` | `salemus` | `\dialectform{salemus}{sal\rfeStress{e}mus}` | compilación 44, p. 37-38 |
| 23 | `kantábamus` | `cantabamus` | `\dialectform{cantabamus}{kant\rfeStress{a}bamus}` | compilación 44, p. 37-38 |
| 23 | `kedrémus` | `quedremus` | `\dialectform{quedremus}{kedr\rfeStress{e}mus}` | compilación 44, p. 37-38 |
| 23 | `tubjéndu` | `tubjendu` | `\dialectform{tubjendu}{tubj\rfeStress{e}ndu}` | compilación 44, p. 37-38 |
| 23 | `dišjéndu` | `dixjendu` | `\dialectform{dixjendu}{diSj\rfeStress{e}ndu}` | compilación 44, p. 37-38 |
| 23 | `abrábiníu` | `abrá biníu` | `\dialectform{abrá biníu}{abr\rfeStress{a} bin\rfeStress{i}u}` | compilación 44, p. 37-38 |
| 23 | `gwḯnü` | `güinu` | `\dialectform{güinu}{gw\rfeStressedMixedI n\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `málü` | `malu` | `\dialectform{malu}{m\rfeStress{a}l\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `agwḯlü` | `agüilu` | `\dialectform{agüilu}{agw\rfeStressedMixedI l\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `sǘrdü` | `surdu` | `\dialectform{surdu}{s\rfeStressedMixedU rd\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `sǘstü` | `sustu` | `\dialectform{sustu}{s\rfeStressedMixedU st\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `pǘnü` | `punu` | `\dialectform{punu}{p\rfeStressedMixedU n\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `rḯjü` | `riyu` | `\dialectform{riyu}{r\rfeStressedMixedI j\rfeMixedU}` | compilación 44, p. 37-38 |
| 23 | `tḯjü` | `tiyu` | `\dialectform{tiyu}{t\rfeStressedMixedI j\rfeMixedU}` | compilación 44, p. 37-38 |
| 24 | `éstu` | `estu` | `\dialectform{estu}{\rfeStress{e}stu}` | compilación 44, p. 38 |
| 24 | `éθę` | `ece` | `\dialectform{ece}{\rfeStress{e}T\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `áθę` | `ace` | `\dialectform{ace}{\rfeStress{a}T\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `pulúkę` | `puluque` | `\dialectform{puluque}{pul\rfeStress{u}k\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `ísẹ` | `isi` | `\dialectform{isi}{\rfeStress{i}s\rfeRelaxedClosed}` | compilación 44, p. 38 |
| 24 | `pelébra` | `pelebra` | `\dialectform{pelebra}{pel\rfeStress{e}bra}` | compilación 44, p. 38 |
| 24 | `ésu` | `esu` | `\dialectform{esu}{\rfeStress{e}su}` | compilación 44, p. 38 |
| 24 | `póku` | `pocu` | `\dialectform{pocu}{p\rfeStress{o}ku}` | compilación 44, p. 38 |
| 24 | `ášu` | `axu` | `\dialectform{axu}{\rfeStress{a}Su}` | compilación 44, p. 38 |
| 24 | `púθu` | `puzu` | `\dialectform{puzu}{p\rfeStress{u}Tu}` | compilación 44, p. 38 |
| 24 | `púθu` | `pucu` | `\dialectform{pucu}{p\rfeStress{u}Tu}` | compilación 44, p. 38 |
| 24 | `tjémbu` | `tiempu` | `\dialectform{tiempu}{tj\rfeStress{e}mbu}` | compilación 44, p. 38 |
| 24 | `kántę` | `cante` | `\dialectform{cante}{k\rfeStress{a}nt\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `tráŋkę` | `tranque` | `\dialectform{tranque}{tr\rfeStress{a}Nk\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `mwírtu` | `muertu` | `\dialectform{muertu}{mw\rfeStress{i}rtu}` | compilación 44, p. 38 |
| 24 | `swéltę` | `suelte` | `\dialectform{suelte}{sw\rfeStress{e}lt\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `majístru` | `mayistru` | `\dialectform{mayistru}{maj\rfeStress{i}stru}` | compilación 44, p. 38 |
| 24 | `ótrę` | `otre` | `\dialectform{otre}{\rfeStress{o}tr\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `tulúndru` | `tulundru` | `\dialectform{tulundru}{tul\rfeStress{u}ndru}` | compilación 44, p. 38 |
| 24 | `pérę` | `pere` | `\dialectform{pere}{p\rfeStress{e}r\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `píru` | `piru` | `\dialectform{piru}{p\rfeStress{i}ru}` | compilación 44, p. 38 |
| 24 | `búrę` | `bure` | `\dialectform{bure}{b\rfeStress{u}r\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `búru` | `buru` | `\dialectform{buru}{b\rfeStress{u}ru}` | compilación 44, p. 38 |
| 24 | `kórę` | `corre` | `\dialectform{corre}{k\rfeStress{o}r\rfeRelaxedPalatal}` | compilación 44, p. 38 |
| 24 | `rodánu` | `rodanu` | `\dialectform{rodanu}{rod\rfeStress{a}nu}` | compilación 44, p. 38 |
| 24 | `šontánu` | `xontanu` | `\dialectform{xontanu}{Sont\rfeStress{a}nu}` | compilación 44, p. 38 |
| 24 | `éstus` | `estus` | `\dialectform{estus}{\rfeStress{e}stus}` | compilación 44, p. 38 |
| 24 | `áθęs` | `aces` | `\dialectform{aces}{\rfeStress{a}T\rfeRelaxedPalatal s}` | compilación 44, p. 38 |
| 24 | `pulúkęs` | `puluques` | `\dialectform{puluques}{pul\rfeStress{u}k\rfeRelaxedPalatal s}` | compilación 44, p. 38 |
| 24 | `pókus` | `pocus` | `\dialectform{pocus}{p\rfeStress{o}kus}` | compilación 44, p. 38 |
| 24 | `ášus` | `axus` | `\dialectform{axus}{\rfeStress{a}Sus}` | compilación 44, p. 38 |
| 24 | `púθus` | `pucus` | `\dialectform{pucus}{p\rfeStress{u}Tus}` | compilación 44, p. 38 |
| 24 | `tjémbus` | `tiempus` | `\dialectform{tiempus}{tj\rfeStress{e}mbus}` | compilación 44, p. 38 |
| 24 | `tráŋkęs` | `tranques` | `\dialectform{tranques}{tr\rfeStress{a}Nk\rfeRelaxedPalatal s}` | compilación 44, p. 38 |
| 24 | `mwírtus` | `muertus` | `\dialectform{muertus}{mw\rfeStress{i}rtus}` | compilación 44, p. 38 |
| 24 | `swéltẹs` | `sueltis` | `\dialectform{sueltis}{sw\rfeStress{e}lt\rfeRelaxedClosed s}` | compilación 44, p. 38 |
| 24 | `tulúndrus` | `tulundrus` | `\dialectform{tulundrus}{tul\rfeStress{u}ndrus}` | compilación 44, p. 38 |
| 24 | `pérus` | `perus` | `\dialectform{perus}{p\rfeStress{e}rus}` | compilación 44, p. 38 |
| 24 | `búręs` | `bures` | `\dialectform{bures}{b\rfeStress{u}r\rfeRelaxedPalatal s}` | compilación 44, p. 38 |
| 24 | `kóręs` | `corres` | `\dialectform{corres}{k\rfeStress{o}r\rfeRelaxedPalatal s}` | compilación 44, p. 38 |
| 24 | `rodánus` | `rodanus` | `\dialectform{rodanus}{rod\rfeStress{a}nus}` | compilación 44, p. 38 |
| 24 | `golós:` | `golós` | `\dialectform{golós}{gol\rfeStress{o}s\rfeLong}` | compilación 44, p. 38 |
| 24 | `sés:` | `ses` | `\dialectform{ses}{s\rfeStress{e}s\rfeLong}` | compilación 44, p. 38 |
| 24 | `iskuplós:` | `iscuplós` | `\dialectform{iscuplós}{iskupl\rfeStress{o}s\rfeLong}` | compilación 44, p. 38 |

Total: **117 formas etiquetadas**.
