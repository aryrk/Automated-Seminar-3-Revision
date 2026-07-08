Learning: Research and Practice
ISSN: 2373-5082 (Print) 2373-5090 (Online) Journal homepage: www.tandfonline.com/journals/rlrp20
Technology-based scaffolding for ill-structured
problem-solving: a systematic review and
emerging directions with AI
Hyeji Jang, Sujin Kim & Hyo-Jeong So
To cite this article: Hyeji Jang, Sujin Kim & Hyo-Jeong So (12 Dec 2025): Technology-based
scaffolding for ill-structured problem-solving: a systematic review and emerging directions with
AI, Learning: Research and Practice, DOI: 10.1080/23735082.2025.2591403
To link to this article: https://doi.org/10.1080/23735082.2025.2591403
Published online: 12 Dec 2025.
Submit your article to this journal
Article views: 2
View related articles
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=rlrp20

LEARNING: RESEARCH AND PRACTICE
https://doi.org/10.1080/23735082.2025.2591403
Technology-based scaffolding for ill-structured
problem-solving: a systematic review and emerging
directions with AI
Hyeji Jang , Sujin Kim and Hyo-Jeong So
Department of Educational Technology, Ewha Womans University, Seoul, Korea
ABSTRACT ARTICLE HISTORY
This study investigates how technology-based scaffolding has Received 20 May 2025
evolved to support learners’ problem-solving skills. Using PRISMA Accepted 25 October 2025
guidelines, 29 articles published between 2014 and 2024 were
KEYWORDS
reviewed across educational levels, methods, technologies, problem
Technology-based
types, and scaffolding mechanisms. Most studies focused on higher scaffolding; ill-structured
education, with limited research on K–12 or adult learners. Methods problem-solving; systematic
largely examined cognitive outcomes through questionnaires and literature review; scaffolding
performance tests. Collaborative technologies were commonly used, in problem-solving;
especially for strategic and design problems in engineering and emerging directions with AI
education. Scaffolding was mainly conceptual and metacognitive,
delivered in non-adaptive text-based formats with little affective
support. Fixed-adding and performance-based adding were the
dominant patterns. The study also highlights the potential of artificial
intelligence to provide more adaptive, personalized, and holistic
scaffolding for future ill-structured problem solving.
Introduction
Problem-solving has become a critical competency for learners in the VUCA (Volatility,
Uncertainty, Complexity, and Ambiguity) era, largely shaped by the Fourth Industrial
Revolution (Poquet & de Laat, 2021). Many contemporary challenges manifest as ill-
structured problems, characterized by unclear definitions and multiple possible solutions
(Tawfik et al., 2018). To navigate these complexities, learners require scaffolding that supports
both cognitive and metacognitive demands. Traditionally, such scaffolding has relied on
guidance from more capable human actors such as parents, teachers, and peers. However,
advances in technology have enabled technology-based scaffolding to play an important role
in supporting deeper learning by facilitating planning, monitoring, and accessing relevant
resources essential for problem-solving. The growing interest in technology-based scaffolding
stems from the increasing demand for flexible support tailored to learners’ individual
characteristics and contextual needs. More recently, artificial intelligence (AI) has further
transformed technology-based scaffolding through adaptive mechanisms that dynamically
adjust the type and degree of assistance based on learners’ responses (Sorour et al., 2024),
making a significant shift in technology-based scaffolding design.
CONTACT Hyo-Jeong So hyojeongso@ewha.ac.kr Department of Educational Technology, Ewha Womans
University, 52 Ewhayeodae-gil, Seodaemun-gu, Seoul 03760, Korea
© 2025 Informa UK Limited, trading as Taylor & Francis Group

2 H. JANG ET AL.
Despite ongoing discussions, there remains a need for a deeper understanding of how
to design and implement technological support in the context of ill-structured problem-
solving. Although emerging technologies, such as generative AI (GenAI), offer opportu-
nities for dynamic and adaptive scaffolding, systematic literature reviews that holistically
examine core design elements, including scaffolding types, delivery methods, and fading
patterns, remain insufficient. Existing research has primarily focused on comparing types
of scaffolding rather than exploring how scaffolding is delivered and enacted in learning
environments (Belland et al., 2017; Kim & Lim, 2019), resulting in limited understand-
ings of scaffolding delivery mechanisms. This narrow focus limits insights into scaffold-
ing delivery mechanisms and how learners regulate their own cognitive processes. There
is a need for research that adopts a more integrated perspective that considers not only
the type of scaffolding provided but also how it is presented and utilized in practices.
To address this gap, the present study conducts a systematic review of empirical
research on technology-based scaffolding in ill-structured problem-solving published
over the past decade (2014–2024). By examining the characteristics and dimensions of
scaffolding across studies, this work aims to provide a comprehensive understanding that
informs future design and implementation of adaptive, technology-enhanced scaffolding
systems.
Literature review
Ill-structured problem-solving
Problem-solving is widely recognized as a fundamental cognitive activity in both daily and
professional contexts (Jonassen, 2000). In general, problems can be categorized into two
types: well-structured and ill-structured. Well-structured problems require the application
of a defined set of concepts, rules, and principles to a specific scenario. In contrast, ill-
structured problems arise in real-world situations with little or no clear solutions and tend
to be more abstract, complex, and cognitively demanding (Jonassen, 1997). A defining
feature of ill-structured problem-solving is the need to justify one’s solution process (Baker,
1999). Argumentation is central to this process, as it enables learners to consider multiple
perspectives, develop and select viable solutions, and substantiate their choices with data
and evidence (Cho & Jonassen, 2002). In doing so, argumentation not only fosters deeper
engagement but also encourages learners to articulate and, when necessary, revise their
underlying beliefs (Baker, 1999). Studies have further explored students’ argumentation in
ill-structured problem-solving through the use of adaptive scaffolding and fading mechan-
isms (Noroozi et al., 2018; Tawfik et al., 2018).
Building on prior research, this study defines ill-structured problems as those that
“possess multiple solutions and solution paths, have fewer manipulable parameters, and
contain uncertainty regarding which concepts, rules, and principles are necessary for the
solution, how they should be organized, and which solution is best” (Jonassen, 1997,
p. 65). For this systematic literature review, we categorize ill-structured problems into six
types: troubleshooting, diagnosis and solution, strategic performance, case analysis,
design, and dilemmas. Table 1 provides detailed descriptions and examples of each.
These categories were selected according to their degree of ill-structuredness (Jonassen,
2000). For example, troubleshooting problems involve identifying system faults by

LEARNING: RESEARCH AND PRACTICE 3
Table 1. Description and examples of problem types (Jonassen, 2000).
Types Descriptions Examples
Troubleshooting Diagnosing system malfunctions by correlating symptoms with fault Troubleshooting an
states, using an iterative process of hypothesis generation and inoperative car or
testing to refine their understanding. computer
Diagnosis Identifying faults in a complex system, selecting and evaluating Medical diagnosis and
solution treatment options, and measuring success based on the strategy treatment
used, the treatment’s effectiveness, and its justification within
a structured, real-world context.
Strategic Intricate and interconnected activity structures in real-time, where Flying an airplane in
performance students employ multiple strategies to adhere to a more intricate a combat mission
and ambiguous strategy while upholding awareness of the
situation.
Case analysis A systematic process encompassing goal clarification, data collection, Analyzing law cases
hypothesis formulation, forecasting, planning, decision-making,
monitoring the consequences of actions, and self-reflection.
Design Unclear goal specifications, absence of a predetermined solution Designing a bridge
path, and the necessity to integrate knowledge from multiple
domains.
Dilemmas Complicated social scenarios involving conflicting perspectives Ethical dilemmas in AI
typically represent the most challenging and perplexing problems.
generating and testing hypotheses, whereas dilemmas represent the most ill-structured
type, characterized by the absence of universally acceptable solutions and the involve-
ment of stakeholders with conflicting moral values.
Technology-based scaffolding in ill-structured problem-solving
Scaffolding plays a crucial role in ill-structured problem-solving, which requires learners
to engage with both domain-specific knowledge and structured problem-solving strate-
gies (Ge & Land, 2004). Rooted in Vygotsky’s Zone of Proximal Development (ZPD),
Wood et al. (1976) conceptualized scaffolding as “enabling a child or novice to solve
a problem, carry out a task, or achieve a goal which would be beyond his unassisted
efforts” (p. 90). In technology-integrated learning environments, Saye and Brush (2002)
identified two types of scaffolding for ill-structured problem-solving: hard scaffolds and
soft scaffolds. Hard scaffolds are pre-designed, static support mechanisms that anticipate
common challenges students may encounter throughout the problem-solving process. In
contrast, soft scaffolds are dynamic and situational, adjusting support in real time based
on learners’ needs. Soft scaffolds are commonly implemented in adaptive learning
systems where support is provided either in response to learners’ requests or as the
system detects difficulties through interactions (Lin et al., 2022; Pan & Liu, 2022).
Technology-based scaffolding can be further categorized based on its intended
purposes. Cagiltay (2006) proposed four types of scaffolding: conceptual (supportive),
metacognitive (reflective), procedural, and strategic (intrinsic) scaffolding. Conceptual
scaffolding supports learners by guiding them on what to consider and how to
connect concepts during the problem-solving process, often through hints or cues
that direct them towards possible solutions. Metacognitive scaffolding assists learners
in planning and monitoring their problem-solving process, making reflective thinking
explicit. Procedural scaffolding helps learners navigate available resources and proce-
dures within a given environment to ensure efficient utilization of tools and

4 H. JANG ET AL.
information. Lastly, strategic scaffolding guides problem analysis, including the selec-
tion, use, and adaptation of relevant tools and resources to facilitate problem-solving
processes.
Beyond cognitive scaffolding, recent research has expanded to include affective scaf-
folding to sustain learners’ motivation (Belland et al., 2013). From a sociocultural
perspective, problem-solving is not only a cognitive process but also an affective one
since learners often experience cognitive disequilibrium that triggers affective dynamics
that play a crucial role in restoring cognitive balance and driving persistence (D’Mello &
Graesser, 2012; Mangaroska et al., 2022). As a result, the concept of scaffolding has
evolved beyond solely cognitive support to encompass affective and motivational dimen-
sions, which highlight the interplay between cognition, emotion, and learning in complex
problem-solving contexts.
The effectiveness of technology-based scaffolding is grounded in literature that exam-
ines how learning unfolds and what environments best optimize this process. Dever et al.
(2023) found that learners who received prompt feedback from agent scaffolds in ITS
environments demonstrated greater gains in both outcomes and self-regulatory strate-
gies. In the context of GenAI, Kim et al. (2025) reported that cognitive scaffolding
enhanced engagement and self-efficacy, while Menekse et al. (2025) showed that natural
language–based reflective scaffolding improved the specificity of learners’ reflections,
increased participation, and fostered achievement through interest-driven reflection.
Collectively, these studies highlight that the value of scaffolding extends beyond perfor-
mance outcomes, addressing the broader question of how to support and orchestrate
learning processes. Recent research has further clarified the mechanisms by which
scaffolding influences cognitive and metacognitive strategies, self-regulation, and affec-
tive engagement, often employing real-time data tracking and adaptive support design
(Lin et al., 2022; Wang et al., 2023). Increasingly, scaffolding is positioned not merely as
a supportive tool but as a central framework for explaining learning mechanisms and
informing the design of technology-enhanced learning environments.
In ill-structured problem-solving, where neither the necessary information nor
the solution processes are explicitly defined, it is crucial to consider multiple
scaffolding aspects in alignment with the problem’s characteristics. Recent studies
have employed GenAI to support students’ ill-structured problem-solving. Liao
et al. (2024) developed a GPT-based scaffolding system for programming education
to enhance students’ computational thinking skills and examined its effects. The
system consisted of three modules: solution assessment, code assessment, and free
interaction. The experimental group that used the scaffolding system demonstrated
improvements in computational thinking and expressed positive perceptions of the
system’s utility for programming education. In addition, Liu et al. (2026) developed
a GenAI chatbot that provides adaptive metacognitive scaffolding during program-
ming education and compared its effects with those of planned, paper-based
metacognitive scaffolding. The GenAI chatbot detects students’ behavioural patterns
and provides context-aware prompts. The results indicated that students who used
the GenAI chatbot showed significant improvements in computational thinking
performance and experienced a reduction in intrinsic cognitive load during pro-
blem-solving.

LEARNING: RESEARCH AND PRACTICE 5
Some researchers have conducted systematic literature reviews. For instance, Jamari
et al. (2017) examined scaffolding strategies in ill-structured problem-solving across
educational levels, platforms, and strategies commonly used in these contexts. Their
findings indicated that metacognitive scaffolding was predominantly employed in higher
education institutions, often implemented through formal platforms such as Learning
Management Systems (LMS). More recently, Sun et al. (2024) conducted a literature
review on Technology-Supported Scaffoldings (TSS) for primary and secondary school
learners. They found that most technological tools employed in TSS were e-learning-
based, with limited reports on the potential of emerging technologies such as AI and
augmented reality. They also highlighted that metacognitive scaffolding was predomi-
nantly delivered on fixed schedules, thereby restricting opportunities for learners to
exercise autonomy in selecting when and how to receive support.
The present study
While existing reviews offer valuable insights into scaffolding mechanisms, there remains
a limited understanding of how technology-based scaffolding can be intentionally
designed and implemented to support learners in ill-structured problem-solving. As
GenAI becomes increasingly integrated into educational contexts, it is important to
investigate how intelligent scaffolding strategies can provide personalized and adaptive
support. Effective scaffolding involves not only offering timely assistance but also gradual
fading of support to promote learners’ problem-solving abilities (Pea, 2004). However,
current systematic reviews often fail to address how technology-based scaffolding is both
enacted and faded in learning environments.
To address this gap, the present study conducted a systematic review of empirical
research to identify how technology-based scaffolding supports ill-structured problem-
solving in educational settings. Beyond categorizing scaffolding types, this study explores
critical dimensions such as adaptivity, modality, and patterns of scaffolding change to
provide a more comprehensive understanding of how technology-based scaffolding can
be designed and implemented to support complex problem-solving processes. This
research is guided by the following questions:
RQ1: What are the research trends in empirical studies on technology-based scaffold-
ing in ill-structured problem-solving?
RQ2: What are the characteristics of empirical studies on technology-based scaffolding
in ill-structured problem-solving (e.g., research methods, problem type, and technol-
ogy type)?
RQ3: What are the key aspects of technology-based scaffolding in ill-structured pro-
blem-solving (e.g., scaffolding type, adaptivity, modality, and change patterns)?
By addressing these questions, this study aims to provide a comprehensive understanding
of how technology-based scaffolding can be designed to effectively support learners in
navigating complex problem-solving scenarios.

6 H. JANG ET AL.
Methods
Literature search and selection
Relevant articles for the systematic literature 7review were identified from three
major academic databases: ERIC, Scopus, and Web of Science. The search process
was conducted using the main keywords “problem-solving” combined with “scaf-
fold” OR “scaffolding” OR “support” and “education” OR “learning”, published
from January 2014 to December 2024. A set of inclusion and exclusion criteria
was applied to identify articles relevant to this review. First, only empirical studies
were included, as these allow for detailed analysis of research methods, ill-
structured problems, and scaffolding practices. Conceptual papers and review arti-
cles were excluded for this reason. Second, only peer-reviewed journal articles
written in English were considered to maintain consistency and rigour in the
analysis. Conference papers and reports were excluded, as they typically lack the
same level of peer review and methodological detail. Third, the review focused on
studies conducted in educational contexts that explicitly addressed scaffolding in ill-
structured problem-solving, with particular emphasis on the use of technology-
based scaffolding mechanisms. Fourth, we also included early access publications
due to the limited number of eligible studies.
To ensure a rigorous selection of relevant articles, we followed the Preferred Reporting
Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (Page et al.,
2021). Two researchers independently screened all retrieved articles from the databases
and cross-checked the inclusion and exclusion criteria to systematically finalize the
selection. As illustrated in Figure 1, the identification phase began with an initial pool
of 9,933 articles collected from three databases. During the screening phase, 4,330
duplicate articles were removed. Next, the titles and abstracts of the remaining articles
were screened, leading to the exclusion of 5,541 articles that were unrelated to the
purpose of this review. Most of the excluded studies focused on well-structured problem
solving, non-technological scaffolding, systematic reviews, or conceptual research that
were not empirical. After the initial title and abstract screening, 65 articles were retained
for full-text review. Of these, 36 were excluded for meeting the exclusion criteria (see
Figure 1 for detailed criteria), resulting in a final set of 29 articles included in this review
(see Appendix for the complete list of references).
Coding framework
As shown in Table 2, the coding framework for this review includes six main categories:
(1) publication year, (2) education level, (3) research method, (4) technology, (5) ill-
structured problem, and (6) scaffolding. The first three categories focus on basic descrip-
tive information about each study, while the latter three examine the key aspects of
technology-based scaffolding in ill-structured problem-solving.
For the basic information, publication years were coded according to the year each
article was published. Education levels were categorized to encompass all levels of formal
education, from elementary to higher education, as well as adult education and other
learning contexts. Research methods were analysed by considering both research vari-
ables and data collection methods. Research variables were broadly classified into

LEARNING: RESEARCH AND PRACTICE 7
Figure 1. PRISMA flowchart of the literature selection process.
cognitive, affective, and other categories. Data collection methods included interviews,
log data, observations, questionnaires, and tests.
The analysis of technology-based scaffolding focused on three aspects: (a) types of
technology, (b) types of ill-structured problems, and (c) scaffolding mechanisms.
Technology types refer to the main technology used in the learning environment to
provide scaffolding, such as AI, collaborative, and virtual technology. Ill-structured
problems were coded in terms of both problem types and domains. Problem types
followed Jonassen’s (2000) typology, which includes case analysis, design problems,
diagnosis-solution, dilemmas, strategic performance, and troubleshooting (refer to
Table 1). Problem domains were coded using a bottom-up approach to identify disci-
plinary fields such as natural science, social science, and engineering.

8 H. JANG ET AL.
Table 2. Coding framework.
Category Criteria
Publication year From 2014 to 2024
Education level 1. Elementary education 2. Secondary education
3. Higher education 4. Adult education 5. Others
1. Cognitive load 2. Interaction
3. Learning engagement patterns
Cognitive 4. Learning performance
5. Metacognition
6. Prior knowledge
Research variable
Research* methods 7. Problem-solving ability
1. Academic emotion
Affective 2. Efficacy
3. Motivation
4. Satisfaction
5. Others
Others
Data collection method 1. Interview 2. Log data 3. Observation
4. Questionnaire 5. Test
1. Artificial intelligence (AI)
2. Collaborative technology
Technology Type 3. Intelligent tutoring system (ITS)
4. Virtual technology
5. Visualization technology
Problem type 1. Case analysis 2. Design
3. Diagnosis-solution 4. Dilemma
Ill-structured problem 5. Strategic performance 6. Troubleshooting
Problem 1. Natural science 2. Social science 3. Education
domain 4. Engineering 5. English 6. Medicine 7. Career
1. Supportive (conceptual)
Type* 2. Reflective (metacognitive)
3. Procedural 4. Strategic (intrinsic) 5. Affective
Adaptivity 1. Adaptive 2. Non-adaptive 3. Mixed
Modality* 1. Text-based 2. Visualization-based
Scaffolding
3. Multimodality-based
Fixed
1. Fixed fading 2. Fixed adding
3. Fixed adding and fading
Change patterns* Performance-based
4. Performance-based fading
5. Performance-based adding
6. Performance-based adding and fading
Self-selected
7. Self-selected fading 8. Self-selected adding
9. Self-selected adding and fading
*Duplicate coding was allowed for research methods and scaffolding.
Scaffolding mechanisms were analysed in four key components: (a) scaffolding type,
(b) adaptivity, (c) modality, and (d) change patterns. Scaffolding types were classified
using Cagiltay’s (2006) framework, which includes conceptual (supportive), metacogni-
tive (reflective), procedural, and strategic (intrinsic), with the addition of affective
scaffolding. The adaptivity of scaffolding delivery methods was categorized as adaptive,
non-adaptive, or mixed. Scaffolding modality was coded as text-based, visualization-
based, or multimodality-based. Text-based scaffolding includes question prompts, hints,
messages, resources, exams, templates, and checklists. Visualization-based scaffolding
encompasses graphic organizers and monitoring visualizers. Multimodality-based scaf-
folding includes annotation, classification labels, and video tutorials. Lastly, scaffolding
change patterns were analysed using the framework by Sun et al. (2024) to examine how

LEARNING: RESEARCH AND PRACTICE 9
scaffolding is faded, added, or combined. Change patterns were classified into fixed,
performance-based, and self-selected scaffolding. Fixed scaffolding follows predeter-
mined time intervals for adding or removing scaffolding. Performance-based scaffolding
dynamically adjusts support based on learners’ performance, such as dynamic assess-
ment. Self-selected scaffolding occurs when learners take the initiative to request or
remove support according to their individual needs.
Results
Publication year and education level
The publication years reflect the distribution of the literature from 2014 to 2024. As
illustrated in Figure 2, the number of studies shows a steady upward trend over the past
decade, with a significant increase in 2024, suggesting a growing research interest in
technology-based scaffolding for ill-structured problem-solving. The education level of
study participants is presented in Figure 3. The results indicate that the majority of
articles (80%) were conducted in higher education settings, while research in K-12
schools and other learning environments remains comparatively limited.
Research methods
Table 3 shows the analysis of research methods, focusing on research variables and data
collection methods. Regarding research variables, cognitive variables were the most frequently
measured, with problem-solving ability emerging as the most commonly investigated con-
struct (n = 14, 28.6%). Among affective variables, satisfaction was the most commonly
measured (n=8, 53.3%). Other variables included usability, epistemic belief, and psychomotor
skills. Regarding data collection methods, tests and questionnaires were most widely used.
Questionnaires examining learners’ satisfaction with designed scaffolding environments were
Figure 2. Publication year.

10 H. JANG ET AL.
Figure 3. Education level (n=29).
Table 3. Research methods.
| Category         | Sub-category | Criteria                | Frequency | %    |
| ---------------- | ------------ | ----------------------- | --------- | ---- |
| Research         | Cognitive    | Problem-solving ability | 14        | 28.6 |
| Variable         |              | Learning performance    | 12        | 24.5 |
|                  |              | Prior knowledge         | 9         | 18.4 |
|                  |              | Metacognition           | 5         | 10.2 |
|                  |              | Learning engagement     | 4         | 8.2  |
|                  |              | Interaction             | 4         | 8.2  |
|                  |              | Cognitive load          | 1         | 2.0  |
|                  |              | Total                   | 49        | 100  |
|                  | Affective    | Satisfaction            | 8         | 53.3 |
|                  |              | Efficacy                | 3         | 20.0 |
|                  |              | Motivation              | 1         | 6.7  |
|                  |              | Academic emotion        | 1         | 6.7  |
|                  |              | Others                  | 2         | 13.3 |
|                  |              | Total                   | 15        | 100  |
|                  | Others       |                         | 4         | 100  |
| Data collection  |              | Questionnaire           | 20        | 33.3 |
| method           |              | Test                    | 19        | 31.7 |
|                  |              | Interview               | 9         | 15.0 |
|                  |              | Log data                | 7         | 11.7 |
|                  |              | Observation             | 5         | 8.3  |
|                  |              | Total                   | 60        | 100  |
the most prevalent (n=20, 33.3%). Tests assessing students’ ill-structured problem-solving
abilities were also commonly used (n = 19, 31.7%). Overall, these results highlight a dominant
reliance on cognitive factors coupled with self-reported data and performance-based assess-
ments in the existing literature.
Technology types
As shown in Table 4, collaborative technology emerges as the most predominant type of
technology used in technology-based scaffolding for ill-structured problem-solving.

LEARNING: RESEARCH AND PRACTICE 11
Table 4. Technology used to provide scaffolding (n=30).
Criteria Frequency %
Collaborative technology 10 33.3
Intelligent tutoring system (ITS) 6 20.0
Visualization technology 6 20.0
Artificial intelligence (AI) 5 16.7
Virtual technology 3 10.0
Representative examples include collaborative problem-solving systems (Lin et al., 2022;
Ouyang et al., 2023), computer-supported collaborative learning (CSCL) environments
(Shin et al., 2020), and inquiry network systems (Shin et al., 2017). These platforms
emphasize peer interaction and shared knowledge construction, highlighting the value of
collaboration in navigating complex problem contexts. The second most common type is
the intelligent tutoring system (ITS), as seen in studies such as Jennings and Muldner
(2021), Hidayah et al. (2019), and Hung et al. (2015). ITS platforms typically provide
adaptive scaffolding by continuously monitoring learners’ responses and tailoring
instructional support to their needs to offer more personalized learning experiences.
A key trend in 2024 was the growing integration of AI-driven scaffolding systems,
as evidenced by four studies that explicitly incorporated artificial intelligence. For
instance, Hu (2024) developed a chatbot-based virtual learning companion using
GenAI to facilitate TAPPS (Think Aloud Pair Problem Solving). In this system,
chatbot-based AI functioned as peer-learning agents to support learners in problem-
solving activities. Similarly, Liao et al. (2024) introduced a chatbot-based coding
support tool designed to enhance learners’ computational thinking using the GPT-
3.5 API. This tool provided iterative cognitive support and feedback across various
problem-solving phases, including decomposition, abstraction, algorithm develop-
ment, and debugging.
Problem types and domains
As shown in Table 5, strategic performance problems were most commonly examined in
the reviewed articles (n = 11, 37.9%). These problems typically require learners to devise
strategies in complex and uncertain contexts. For example, Tawfik et al. (2018) investi-
gated how learners developed strategies to balance personal selling with technical exper-
tise in new markets, while Oka et al. (2024) explored how novice programmers generated
solution candidates for natural language programming tasks through trial-and-error
problem-solving. The second most common problem type was design problems (n = 7,
24.1%), which involved creating original solutions for ill-defined problems.
Representative examples include creating online teaching strategies for specific case
scenarios (Ouyang et al., 2021) and developing lesson plans to enhance telemarketer
performance in a home shopping company (Shin & Song, 2016).
With respect to disciplinary domains, engineering (n = 8, 27.6%) was the most
frequently explored domain, followed by education (n = 7, 24.1%) and medicine (n =
4, 13.8%), reflecting a strong emphasis on problem-solving competence in applied and
professional contexts.

12 H. JANG ET AL.
Table 5. Ill-structured problem types and domains (n=29).
| Category  | Criteria              | Frequency | %    |
| --------- | --------------------- | --------- | ---- |
| Types of  | Strategic performance | 11        | 37.9 |
| problem   | Design                | 7         | 24.1 |
|           | Case analysis         | 6         | 20.7 |
|           | Diagnosis-solution    | 2         | 6.9  |
|           | Dilemma               | 2         | 6.9  |
|           | Troubleshooting       | 1         | 3.4  |
| Problem   | Engineering           | 8         | 27.6 |
| domain    | Education             | 7         | 24.1 |
|           | Medicine              | 4         | 13.8 |
|           | Career                | 3         | 10.3 |
|           | Natural science       | 3         | 10.3 |
|           | Social science        | 3         | 10.3 |
|           | English               | 1         | 3.4  |
Scaffolding
Key dimensions
To systematically analyse the scaffolding provided during ill-structured problem-solving,
we examined four key dimensions: (a) scaffolding type, (b) adaptivity, (c) modality, and
(d) change patterns. Firstly, the analysis of scaffolding types revealed that supportive
(conceptual) scaffolding was the most commonly used, accounting for 41% (n = 25) of
the reviewed studies (see Figure 4). Supportive (conceptual) scaffolding primarily
assisted learners in understanding what to focus on and how to connect different
concepts during problem-solving. For instance, Kim and Lim (2019) designed scaffolding
about relevant concepts that learners need to consider when planning instructional
design. The second most frequent type was reflective (metacognitive) scaffolding (n =
16, 29.1%), which supported learners to plan, monitor, and regulate their problem-
solving processes by prompting reflection and self-assessment. For instance, Winkler
et al. (2021) used a Smart Personal Assistant in business management school courses to
facilitate the internalization of the problem-solving process by supporting learners’
Figure 4. Scaffolding type (n=55).

LEARNING: RESEARCH AND PRACTICE 13
reflection and negotiation. In contrast, affective scaffolding was rarely utilized, with only
one study (Zheng et al., 2022) providing appropriate prompts based on the emotions
expressed by participants, such as positive, negative, neutral, and confused, in an online
collaborative programming course.
Regarding adaptivity, Figure 5 shows that most scaffolding mechanisms were non-
adaptive (n = 17, 58.6%), followed by adaptive (n = 9, 31.0%) and mixed approaches (n =
3, 10.3%). Non-adaptive scaffolding mechanisms remain static throughout the learning
process rather than dynamically adjusting based on learners’ needs. For instance, Wang
et al. (2023) provided six fixed scaffolding tools, such as “Add Evidence”, “Add Test”, and
“Link Evidence”, without dynamic adjustments. Similarly, Ouyang et al. (2021) inte-
grated scaffolding resources and problem-based learning procedures in a fixed schedule
(e.g., updated every 10 minutes) in audio and text formats as a structured scaffolding
approach.
As shown in Figure 6, text-based scaffolding delivered in the form of question
prompts, hints, and instructional messages was the most frequently used, accounting
for 66.6% (n = 26) of the reviewed studies. For example, Park et al. (2020) implemented
the explanation-based prompt that required students to justify why a particular solution
was ineffective in a given context, and the difference-based prompt that guided students
to distinguish key differences between cases. Visualization-based scaffolding appeared in
fewer studies, with graphic organizers being the most common (n = 7). As an example,
Wang et al. (2018) supported students in constructing mental maps to enhance logical
reasoning, while Shin and Song (2016) provided a content tree to help learners under-
stand the relationships between key concepts and design elements.
Lastly, Figure 7 presents the analysis of scaffolding change patterns. The most pre-
valent methods were fixed adding and performance-based adding, collectively account-
ing for 66.7% of the reviewed articles. Fixed adding refers to scaffolding that is
predetermined and provided at specific points where support is necessary during the
problem-solving process. For example, Shin et al. (2017) implemented fixed color-coded
scaffolding as a study guide while Hung et al. (2015) provided learners with a glossary
Figure 5. Scaffolding adaptivity (n=29).

14 H. JANG ET AL.
Figure 6. Scaffolding modality (n=39).
Figure 7. Scaffolding change patterns (n=33).
and audiovisual presentation of research concepts throughout the learning experience.
Performance-based adding, on the other hand, offers personalized scaffolds that dyna-
mically adjust based on learners’ responses or performance. Hidayah et al. (2019)
grouped learners based on the metacognitive awareness inventory (MAI) data and
provided metacognitive hints customized to each group. Pan and Liu (2022) implemen-
ted pop-up messages that adapted to learners’ problem-solving progress to provide
contextually relevant support. In contrast, self-selected adding and fading, which gives

LEARNING: RESEARCH AND PRACTICE 15
more agency to learners, rarely appeared in the literature. The self-selected mechanism
allows learners to control their scaffolding experience by requesting or dismissing
scaffolding features as needed. For instance, Shin et al. (2020) developed a mechanism
where learners could click to view key terms necessary for solving a problem, with the
option to open and close the keyword section based on individual needs.
Overall trends
To illustrate broader patterns across the reviewed studies, a Sankey diagram was created
to map the relationships among technology type, scaffolding type, modality, and adap-
tivity. As shown in Figure 8, conceptual and metacognitive scaffolding were the most
frequently employed, appearing in more than half of the studies across technology
categories. In contrast, affective scaffolding was almost absent, observed in only one
study, and delivered in a text-based format. Across modalities, scaffolding was predomi-
nantly provided through text-based mechanisms such as prompts, hints, and instruc-
tional messages, with limited use of visualization or multimodal approaches. Moreover,
most scaffolding was delivered in a non-adaptive manner. Even in the relatively few cases
where adaptive scaffolding was implemented, it was exclusively text-based, with no
evidence of adaptive visualization-based or multimodal scaffolds. Overall, the findings
suggest that technology-based scaffolding in ill-structured problem-solving has largely
relied on fixed, pre-designed forms of support, with limited attention to dynamic
adaptation.
To further investigate the effect of scaffolding on learning outcomes, we analysed four
studies that compared the impact of different scaffolding types. Three of these studies
reported positive effects of metacognitive scaffolding. For example, Shin and Song (2016)
reported that learners who received metacognitive scaffolding outperformed those
receiving conceptual scaffolding in problem representation and solution development.
Figure 8. Sankey diagram of technology-based scaffolding in ill-structured problem-solving.

16 H. JANG ET AL.
Similarly, Kim and Lim (2019) found that metacognitive scaffolding had significant
positive effects on cognitive and social presence, as well as on problem representation,
monitoring, and evaluation, compared with conceptual scaffolding. Wang et al. (2023)
also demonstrated that learners who relied more on metacognitive scaffolding achieved
higher confidence judgements and diagnostic performance, whereas those using con-
ceptual or strategic scaffolding did not show significant gains. In contrast, Ouyang et al.
(2021) found that conceptual scaffolding led to the strongest outcomes in terms of
problem-solving performance and perceptions of group collaboration. Learners receiving
conceptual scaffolding reported the most positive views of collaborative quality, followed
by those in the strategic scaffolding and minimal guidance conditions.
Collectively, these findings suggest that most of the studies applied conceptual and
metacognitive scaffolding. While conceptual scaffolding can enhance collaborative qual-
ity and task performance, metacognitive scaffolding tends to provide broader benefits for
regulation, reflection, and problem-solving performance.
Discussion
This systematic literature review analysed empirical studies on technology-based scaf-
folding in ill-structured problem-solving published from 2014 to 2024. In this section, we
revisit the research questions and discuss the key implications of the main findings.
The first key finding concerns the overall research trend, indicating a steady increase
in research on technology-based scaffolding in ill-structured problem-solving, with
a sharp increase in publications in 2024. This trend reflects the growing integration of
large language models (LLMs), application programming interfaces (APIs), and virtual
reality (VR) in educational settings, which have facilitated the development of persona-
lized and immersive problem-solving environments. Most studies were conducted at the
postsecondary level, with relatively fewer studies examining its implementation in
elementary, secondary, or adult education contexts. This trend may be linked to the
nature of ill-structured problem-solving, which requires advanced cognitive processing
and domain-specific knowledge (Jonassen, 2000). However, as problem-solving skills are
essential competencies for all learners (2015), this finding underscores the need for more
empirical research on technology-based scaffolding in diverse settings. Expanding
research in these areas could provide valuable insights into how scaffolding strategies
can be effectively adapted to diverse learning needs and developmental stages.
A second key finding concerns the imbalance between cognitive and affective dimen-
sions of scaffolding. The strong focus on cognitive aspects of learning is also reflected in the
data collection methods and the types of technology used. Most studies prioritized asses-
sing learners’ problem-solving abilities over affective factors, highlighting a gap in research
on how scaffolding can support learners’ emotional and motivational needs during ill-
structured problem-solving. Yet, emotion plays a critical role in cognitive strategies and
motivational engagement (Pekrun, 1992; Zhou, 2013). Although emotion recognition
systems are advancing, relatively few studies have investigated how AI can provide
adaptive, personalized interventions that address affective states (Septiana et al., 2024).
Given the intricate interaction between affect and the cognitive problem-solving process,
scaffolding should adopt a more integrated approach that extends beyond cognitive
support to promote learner autonomy and motivation. Promising directions include

LEARNING: RESEARCH AND PRACTICE 17
embodied conversational agents (Zhang & Pan, 2025) that provide emotional and motiva-
tional support. By developing a virtual character for the embodied conversational agent, it
is possible to support learners’ immersion and emotional interaction. The agent can
interact in a human-like manner through expressions and gestures, thereby enhancing
immersion, emotional connection, and timely intervention (Mercado et al., 2023).
In terms of problem types, this review found that strategic performance and design
problems were most commonly studied. The frequent focus on strategic performance
problems, such as programming-related challenges, may be attributed to their struc-
tured nature, which allows learners to predict outputs and identify errors during
programming tasks (Jennings & Muldner, 2020). Additionally, design problems were
widely explored as examples of ill-structured problems in the literature (e.g., Kim &
Lim, 2019; Ouyang et al., 2021; Shin et al., 2020). These design problems were
employed to enhance learners’ practical skills in instructional design, aligning to
prepare them for real-world challenges and tasks (Shin & Song, 2016). Regarding
technology types, we observed a growing integration of AI-assisted scaffolding to
provide more adaptive and personalized learning experiences, representing
a significant shift from traditional static scaffolding models. The increasing use of
collaborative technology also underscores the importance of peer interaction and
shared cognitive processes in facilitating problem-solving.
This review also provides an analysis of key aspects of technology-based scaffolding in
ill-structured problem-solving, including scaffolding type, adaptivity, modality, and
change patterns. The findings indicate that conceptual and metacognitive scaffolding
were the most commonly provided to support domain knowledge and guide learners’
thinking processes during problem-solving. Metacognitive scaffolding demonstrates
particularly strong effects on problem representation, monitoring, and evaluation (Kim
& Lim, 2019; Shin & Song, 2016; Wang et al., 2023). Conceptual scaffolding, however,
was found to enhance task completion and perceptions of collaborative quality (Ouyang
et al., 2021). These findings suggest that each scaffolding type offers distinct benefits at
different stages of problem-solving, pointing to the need for future research that com-
pares the combined effects of conceptual and metacognitive scaffolding rather than
treating them in isolation (Bulu & Pedersen, 2010).
Most scaffolding mechanisms identified in this review were non-adaptive and text-
based, typically delivered as predesigned prompts or questions created by experts.
However, as AI-driven scaffolding research expands, there is a shift towards adaptive
and personalized learning experiences. For instance, Hybrid Human–AI Regulation
highlights AI’s role in supporting learners’ self-regulated learning (SRL) by guiding
strategy selection and control throughout the learning process (Molenaar, 2022).
Within this emerging paradigm, scaffolding design evolves beyond fixed supports or AI-
generated recommendations based solely on static learning data. Instead, future solutions
need to support learners’ agency in managing their own learning strategies and control
mechanisms during problem-solving. A particularly critical area is adaptive fading. Once
learners demonstrate sufficient independence, scaffolding should be systematically
reduced to promote autonomy and SRL (Lajoie, 2005). Refining adaptive fading requires
careful analysis of learners’ progress to determine which scaffolding elements are bene-
ficial and which can be dynamically withdrawn based on individual needs.

18 H. JANG ET AL.
Further, a particularly promising direction is proactive AI, which provides personalized
recommendations by interpreting model outputs in relation to learner behaviour and,
when necessary, initiating specific actions (Meurisch et al., 2020). Recent studies highlight
its potential in education. Yang and Jung (2025), for example, developed an AI tutor for
online lectures that allowed learners to adjust the level of proactivity; the system could
pause lectures to deliver critical content and support progress monitoring. Similarly, Pu
et al. (2025) introduced an intelligent agent for programming education that intervened
when learners displayed signs of low workload, reached task boundaries, or exhibited
implicit cues of difficulty. Applied to ill-structured problem-solving, proactive AI offers the
possibility of scaffolding that is both adaptive and dynamically faded. The key challenge is
determining when to intervene and how to tailor fading to learners’ evolving needs. With
advances in LLM, proactive AI can increasingly identify learners’ problem-solving stages
through their written responses and provide context-sensitive scaffolds. Over time, such
systems could gradually reduce support in a personalized manner, helping learners transi-
tion towards independence while maintaining timely, targeted guidance.
Conclusion
This study conducted a systematic literature review of empirical research on technology-
based scaffolding in ill-structured problem-solving published between 2014 and 2024.
The review yielded three major insights: a steady growth in research interest,
a predominant emphasis on cognitive rather than affective support, and a growing
integration of adaptive scaffolding through AI. Overall, these findings underscore the
evolving role of technology in enabling more personalized, adaptive, and potentially
multimodal scaffolding to support learners’ problem-solving processes.
Some limitations of this review should be acknowledged. First, we included only empirical
journal articles to ensure methodological rigour and systematic data management. While this
approach enhanced the reliability of the analysis, it also narrowed the pool of studies available
for review. Future research could broaden the scope to include conference proceedings and
non-empirical studies, thereby capturing a wider range of perspectives. Second, this study did
not examine the effects of scaffolding across different learning contexts, as the available
literature did not systematically address contextual variation. Future work could extend this
review by synthesizing findings across diverse settings, including K–12 education, to provide
a more comprehensive understanding of scaffolding effects.
Despite these limitations, this study contributes valuable insights into how technology-
based scaffolding has been designed and implemented over the past decade. The findings
point to the need for future studies to develop scaffolding approaches that move beyond
static, text-based formats towards adaptive, affect-sensitive, and multimodal solutions. By
leveraging advances in AI and emerging technologies, researchers and practitioners can
design scaffolding that not only supports cognitive processes but also fosters learners’
motivation, self-regulation, and autonomy in navigating complex problem-solving contexts.
Acknowledgments
Portions of this research were presented at the Spring Annual Conference of Korean Association
for Educational Information and Media in Korea.

LEARNING: RESEARCH AND PRACTICE 19
Author contributions
CRediT: Hyeji Jang: Conceptualization, Data curation, Formal analysis, Funding acquisition,
Investigation, Methodology, Project administration, Resources, Validation, Visualization,
Writing – original draft; Sujin Kim: Formal analysis, Visualization, Writing – original draft;
Hyo-Jeong So: Conceptualization, Project administration, Supervision, Writing – review &
editing.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This work was supported by the National Research Foundation of Korea (NRF) grant funded by
the Korea government (MSIT) [No, 2023S1A5B5A19093823].
ORCID
Hyeji Jang http://orcid.org/0009-0009-9207-8174
Hyo-Jeong So http://orcid.org/0000-0002-1713-9653
References
(*) The references are the reviewed studies.
Baker, M. J. (1999). Argumentation and constructive interaction. In P. Coirier & J. Andriessen
(Eds.), Foundations of Argumentative Text Processing (pp. 179–202). University of Amsterdam
Press.
Belland, B. R., Kim, C., & Hannafin, M. J. (2013). A framework for designing scaffolds that
improve motivation and cognition. Educational Psychologist, 48(4), 243–270. https://doi.org/
10.1080/00461520.2013.838920
Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing results from empirical
research on computer-based scaffolding in stem education: A meta-analysis. Review of
Educational Research, 87(2), 309–344. https://doi.org/10.3102/0034654316670999
Bulu, S. T., & Pedersen, S. (2010). Scaffolding middle school students’ content knowledge and ill-
structured problem solving in a problem-based hypermedia learning environment. Educational
Technology Research and Development, 58(5), 507–529. https://doi.org/10.1007/s11423-010-
9150-9
Cagiltay, K. (2006). Scaffolding strategies in electronic performance support systems: Types and
challenges. Innovations in Education and Teaching International, 43(1), 93–103. https://doi.org/
10.1080/14703290500467673
Cho, K. L., & Jonassen, D. H. (2002). The effects of argumentation scaffolds on argumentation and
problem solving. Educational Technology Research and Development, 50(3), 5–22. https://doi.
org/10.1007/BF02505022
Dever, D. A., Sonnenfeld, N. A., Wiedbusch, M. D., Schmorrow, S. G., Amon, M. J., & Azevedo, R.
(2023). A complex systems approach to analyzing pedagogical agents’ scaffolding of self-
regulated learning within an intelligent tutoring system. Metacognition and Learning, 18(3),
659–691. https://doi.org/10.1007/s11409-023-09346-x
D’Mello, S., & Graesser, A. (2012). Dynamics of affective states during complex learning. Learning
and Instruction, 22(2), 145–157. https://doi.org/10.1016/j.learninstruc.2011.10.001

20 H. JANG ET AL.
Ge, X., & Land, S. M. (2004). Scaffolding students’ problem-solving processes in an ill-structured
task using question prompts and peer interactions. Educational Technology Research and
Development, 51(1), 21–38. https://doi.org/10.1007/BF02504515
*Hidayah, I., Adji, T. B., & Setiawan, N. A. (2019). Development and evaluation of adaptive
metacognitive scaffolding for algorithm-learning system. IET Software, 13(4), 305–312. https://
doi.org/10.1049/iet-sen.2018.5072
*Hu, Y. H. (2024). Improving ethical dilemma learning: Featuring thinking aloud pair problem
solving (TAPPS) and AI-assisted virtual learning companion. Education and Information
Technologies, 29(17), 22969–22990. https://doi.org/10.1007/s10639-024-12754-4
*Hung, W. C., Smith, T. J., & Smith, M. C. (2015). Design and usability assessment of a
dialogue-based cognitive tutoring system to model expert problem solving in research design.
British Journal of Educational Technology, 46(1), 82–97. https://doi.org/10.1111/bjet.12125
Jamari, D., Zaid, N. M., Abdullah, Z., Mohamed, H., & Aris, B. (2017). Instructional scaffolding to
support ill-structured problem solving: A review. Sains Humanika, 9(1–4). https://doi.org/10.
11113/sh.v9n1-4.1122
Jennings, J., & Muldner, K. (2020). Assistance that fades in improves learning better than
assistance that fades out. Instructional Science, 48(4), 371–394. https://doi.org/10.1007/
s11251-020-09520-7
*Jennings, J., & Muldner, K. (2021). When does scaffolding provide too much assistance? A
code-tracing tutor investigation. International Journal of Artificial Intelligence in Education,
31(4), 784–819. https://doi.org/10.1007/s40593-020-00217-z
Jonassen, D. H. (1997). Instructional design models for well-structured and ill-structured
problem-solving learning outcomes. Educational Technology Research and Development, 45
(1), 65–94. https://doi.org/10.1007/BF02299613
Jonassen, D. H. (2000). Toward a design theory of problem solving. Educational Technology
Research and Development, 48(4), 63–85. https://doi.org/10.1007/BF02300500
Kim, H., Hwang, J., Kim, T., Choi, M., Lee, D., & Ko, J. (2025). Impact of generative artificial
intelligence on learning: Scaffolding strategies and self-directed learning perspectives.
International Journal of Human-Computer Interaction, 1–23. https://doi.org/10.1080/
10447318.2025.2531267
*Kim, J. Y., & Lim, K. Y. (2019). Promoting learning in online, ill-structured problem solving: The
effects of scaffolding type and metacognition level. Computers and Education, 138, 116–129.
https://doi.org/10.1016/j.compedu.2019.05.001
Lajoie, S. P. (2005). Extending the scaffolding metaphor. Instructional Science, 33(5–6), 541–557.
https://doi.org/10.1007/s11251-005-1279-2
*Liao, J., Zhong, L., Zhe, L., Xu, H., Liu, M., & Xie, T. (2024). Scaffolding computational thinking
with ChatGPT. IEEE Transactions on Learning Technologies, 17, 1627–1642. https://doi.org/10.
1109/TLT.2024.3392896
*Lin, P. C., Hou, H. T., & Chang, K. E. (2022). The development of a collaborative problem solving
environment that integrates a scaffolding mind tool and simulation-based learning: An analysis
of learners’ performance and their cognitive process in discussion. Interactive Learning
Environments, 30(7), 1273–1290. https://doi.org/10.1080/10494820.2020.1719163
Liu, J., Zhang, Y., Li, W., Wang, Q., Niu, P., & Zhang, X. (2026). Adaptive vs. planned metacog-
nitive scaffolding for computational thinking: Evidence from generative AI-supported pro-
gramming in elementary education. Computers and Education, 241(2026), 105473. https://doi.
org/10.1016/j.compedu.2025.105473
Mangaroska, K., Sharma, K., Gašević, D., & Giannakos, M. (2022). Exploring students’ cognitive
and affective states during problem solving through multimodal data: Lessons learned from
a programming activity. Journal of Computer Assisted Learning, 38(1), 40–59. https://doi.org/10.
1111/jcal.12590
Menekse, M., Putra, A. S., Kim, J., Butt, A. A., McDaniel, M. A., Davidesco, I., Cadieux, M., Kim, J.,
& Litman, D. (2025). Enhancing student reflections with natural language processing based
scaffolding: A quasi-experimental study in a large lecture course. Computers and Education:
Artificial Intelligence, 8, 100397. https://doi.org/10.1016/j.caeai.2025.100397

LEARNING: RESEARCH AND PRACTICE 21
Mercado, J., Espinosa-Curiel, I. E., & Martínez-Miranda, J. (2023). Embodied conversational
agents providing motivational interviewing to improve health-related behaviors: Scoping
review. Journal of Medical Internet Research, 25, e52097. https://doi.org/10.2196/52097
Meurisch, C., Mihale-Wilson, C. A., Hawlitschek, A., Giger, F., Müller, F., Hinz, O., &
Mühlhäuser, M. (2020). Exploring user expectations of proactive AI systems. Proceedings of
the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 4(4), 1–22. https://doi.
org/10.1145/3432193
Molenaar, I. (2022). The concept of hybrid human-AI regulation: Exemplifying how to support
young learners’ self-regulated learning. Computers and Education: Artificial Intelligence, 3,
100070. https://doi.org/10.1016/j.caeai.2022.100070
Noroozi, O., Kirschner, P. A., Biemans, H. J., & Mulder, M. (2018). Promoting argumentation
competence: Extending from first-to second-order scaffolding through adaptive fading.
Educational Psychology Review, 30(1), 153–176. https://doi.org/10.1007/s10648-017-9400-z
*Oka, H., Ohnishi, A., Nishida, T., Terada, T., & Tsukamoto, M. (2024). A choice-based program-
ming learning method to develop problem-solving skills. IEEE Access, 12, 119550–119562.
https://doi.org/10.1109/ACCESS.2024.3443879
*Ouyang, F., Chen, Z., Cheng, M., Tang, Z., & Su, C. Y. (2021). Exploring the effect of three
scaffoldings on the collaborative problem-solving processes in China’s higher education.
International Journal of Educational Technology in Higher Education, 18(1), 1–22. https://doi.
org/10.1186/s41239-021-00273-y
*Ouyang, F., Xu, W., & Cukurova, M. (2023). An artificial intelligence-driven learning analytics
method to examine the collaborative problem-solving process from the complex adaptive
systems perspective. International Journal of Computer-Supported Collaborative Learning, 18
(1), 39–66. https://doi.org/10.1007/s11412-023-09387-z
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D.,
Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J.,
Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E.,
McDonald, S., & Moher, D. (2021). The prisma, 2020 statement: An updated guideline for
reporting systematic reviews. Systematic Reviews, 10(1), 1–11. https://doi.org/10.1186/s13643-
021-01626-4
*Pan, Z., & Liu, M. (2022). The role of adaptive scaffolding system in supporting middle school
problem-based learning activities. Journal of Educational Technology Systems, 51(2), 117–145.
https://doi.org/10.1177/00472395221133855
*Park, J., Lee, J., & Kim, D. (2020). The effects of indexing prompts on problem-solving in case
library learning. Problems of Education in the 21st Century, 78(3), 394. https://doi.org/10.33225/
pec/20.78.394
Partnership for 21st Century Skills. (2015). Framework for 21st century learning. http://www.p21.
org/
Pea, R. D. (2004). The social and technological dimensions of scaffolding and related theoretical
concepts for learning, education, and human activity. Journal of the Learning Sciences, 13(3),
423–451. https://doi.org/10.1207/s15327809jls1303_6
Pekrun, R. (1992). The impact of emotions on learning and achievement: Towards a theory of
cognitive/motivational mediators. Applied Psychology, 41(4), 359–376. https://doi.org/10.1111/j.
1464-0597.1992.tb00712.x
Poquet, O., & de Laat, M. (2021). Developing capabilities: Lifelong learning in the age of AI. British
Journal of Educational Technology, 52(4), 1695–1708. https://doi.org/10.1111/bjet.13123
Pu, K., Lazaro, D., Arawjo, I., Xia, H., Xiao, Z., Grossman, T., & Chen, Y. (2025). Assistance or
disruption? Exploring and evaluating the design and trade-offs of proactive AI programming
support. In N. Yamashita, V. Evers, K. Yatani, X. Ding, B. Lee, M. Chetty, & P. Toup-Dugas
(Eds.), Proceedings of the 2025 CHI conference on human factors in computing systems (pp.
1–21). Association for Computing Machinery.
Saye, J. W., & Brush, T. (2002). Scaffolding critical reasoning about history and social issues in
multimedia-supported learning environments. Educational Technology Research and
Development, 50(3), 77–96. https://doi.org/10.1007/BF02505026

22 H. JANG ET AL.
Septiana, A. I., Mutijarsa, K., Putro, B. L., & Rosmansyah, Y. (2024). Emotion-related pedagogical
agent: A systematic literature review. IEEE Access, 12, 36645–36656. https://doi.org/10.1109/
ACCESS.2024.3374376
*Shin, S., Brush, T. A., & Glazewski, K. D. (2017). Designing and implementing web-based
scaffolding tools for technology-enhanced socioscientific inquiry. Journal of Educational
Technology and Society, 20(1), 1–12.
*Shin, S., & Song, H. D. (2016). Finding the optimal scaffoldings for learners’ epistemological
beliefs during ill-structured problem solving. Interactive Learning Environments, 24(8),
2032–2047. https://doi.org/10.1080/10494820.2015.1073749
*Shin, Y., Kim, D., & Song, D. (2020). Types and timing of scaffolding to promote meaningful peer
interaction and increase learning performance in computer-supported collaborative learning
environments. Journal of Educational Computing Research, 58(3), 640–661. https://doi.org/10.
1177/0735633119877134
*Sorour, S. E., Ahmed, R. J., & Abd El Aziz, M. I. (2024). A multi-smart agent-based training
environment for enhancing 3D graphics production and design thinking skills among elemen-
tary computer teachers. Frontiers in Education, 9, 1392266. https://doi.org/10.3389/feduc.2024.
1392266
Sun, D., Chou, K. L., Yang, L., & Yang, Y. (2024). A systematic review of technology-supported
scaffoldings in empirical studies from 2017-2022. Trends, scaffolding design features and
learning outcomes. Educational Technology & Society, 27(3), 185–203.
*Tawfik, A. A., Law, V., Ge, X., Xing, W., & Kim, K. (2018). The effect of sustained vs. faded
scaffolding on students’ argumentation in ill-structured problem solving. Computers in Human
Behavior, 87, 436–449. https://doi.org/10.1016/j.chb.2018.01.035
*Wang, M., Yuan, B., Kirschner, P. A., Kushniruk, A. W., & Peng, J. (2018). Reflective learning
with complex problems in a visualization-based learning environment with expert support.
Computers in Human Behavior, 87, 406–415. https://doi.org/10.1016/j.chb.2018.01.025
*Wang, T., Zheng, J., Tan, C., & Lajoie, S. P. (2023). Computer-based scaffoldings influence
students’ metacognitive monitoring and problem-solving efficiency in an intelligent tutoring
system. Journal of Computer Assisted Learning, 39(5), 1652–1665. https://doi.org/10.1111/jcal.
12824
*Winkler, R., Söllner, M., & Leimeister, J. M. (2021). Enhancing problem-solving skills with smart
personal assistant technology. Computers and Education, 165, 104148. https://doi.org/10.1016/j.
compedu.2021.104148
Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. Journal of Child
Psychology and Psychiatry, 17(2), 89–100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x
Yang, E., & Jung, Y. (2025). Striking the balance: Exploring levels of AI tutor proactivity in
enhancing online self-paced learning. In Companion Proceedings of the 15th International
Conference on Learning Analytics & Knowledge (pp. 263–265). Association for Computing
Machinery.
Zhang, Y., & Pan, W. (2025). A scoping review of embodied conversational agents in education:
Trends and innovations from 2014 to 2024. Interactive Learning Environments, 33(7), 1–22.
https://doi.org/10.1080/10494820.2025.2468972
*Zheng, L., Zhen, Y., Niu, J., & Zhong, L. (2022). An exploratory study on fade-in versus fade-out
scaffolding for novice programmers in online collaborative programming settings. Journal of
Computing in Higher Education, 34(2), 489–516. https://doi.org/10.1007/s12528-021-09307-w
Zhou, M. (2013). “I am really good at it” or “I am just feeling lucky”: The effects of emotions on
information problem-solving. Educational Technology Research and Development, 61(3),
505–520. https://doi.org/10.1007/s11423-013-9300-y

LEARNING: RESEARCH AND PRACTICE 23
Appendix. Reference list of the literature reviewed in this study
1 Berger, J. T., Miller, D. R., & Mooney, M. (2024). Concept mapping: An innovative approach to clinical case analysis
in an undergraduate medical education curriculum in social sciences, humanities, ethics, and professionalism.
Cambridge Quarterly of Healthcare Ethics, 1–7.
2 Chang, C. Y., Panjaburee, P., & Chang, S. C. (2024). Effects of integrating maternity VR-based situated learning into
professional training on students’ learning performances. Interactive Learning Environments, 32(5), 2121–2135.
3 Durley, H. C. K., & Ge, X. (2019). Social discourse influencing elementary teachers’ cognition and metacognition for
problem solving in open-ended professional development. New Waves-Educational Research and Development
Journal, 22(1), 55–71.
4 Girault, I., & d’Ham, C. (2014). Scaffolding a complex task of experimental design in chemistry with a computer
environment. Journal of Science Education and Technology, 23, 514–526.
5 Hidayah, I., Adji, T. B., & Setiawan, N. A. (2019). Development and evaluation of adaptive metacognitive
scaffolding for algorithm‐learning system. IET Software, 13(4), 305–312.
6 Hu (2024). Improving ethical dilemma learning: Featuring thinking aloud pair problem solving (TAPPS) and AI-
assisted virtual learning companion. Education and Information Technologies, 29, 22969–22990.
7 Hung, W. C., Smith, T. J., & Smith, M. C. (2015). Design and usability assessment of a dialogue‐based cognitive
tutoring system to model expert problem solving in research design. British Journal of Educational Technology,
46(1), 82–97.
8 Jennings and Muldner (2021). When does scaffolding provide too much assistance? A code-tracing tutor
investigation. International Journal of Artificial Intelligence in Education, 31, 784–819.
9 Kim and Lim (2019). Promoting learning in online, ill-structured problem solving: The effects of scaffolding type
and metacognition level. Computers & Education, 138, 116–129.
10 Liao, J., Zhong, L., Zhe, L., Xu, H., Liu, M., & Xie, T. (2024). Scaffolding computational thinking with ChatGPT. IEEE
Transactions on Learning Technologies, 17, 1627–1642.
11 Lin, P. C., Hou, H. T., & Chang, K. E. (2022). The development of a collaborative problem solving environment that
integrates a scaffolding mind tool and simulation-based learning: an analysis of learners’ performance and
their cognitive process in discussion. Interactive Learning Environments, 30(7), 1273–1290.
12 Lin, Y. C., Chien, S. Y., & Hou, H. T. (2024). A multi-dimensional scaffolding-based virtual reality educational board
game design framework for service skills training. Education and Information Technologies, 1–28.
13 Oka, H., Ohnishi, A., Nishida, T., Terada, T., & Tsukamoto, M. (2024). A choice-based programming learning method
to develop problem-solving skills. IEEE Access, 12, 119550-119562
14 Ouyang, F., Chen, Z., Cheng, M., Tang, Z., & Su, C. Y. (2021). Exploring the effect of three scaffoldings on the
collaborative problem-solving processes in China’s higher education. International Journal of Educational
Technology in Higher Education, 18(1), 1–22.
15 Ouyang, F., Xu, W., & Cukurova, M. (2023). An artificial intelligence-driven learning analytics method to examine
the collaborative problem-solving process from the complex adaptive systems perspective. International
Journal of Computer-Supported Collaborative Learning, 18(1), 39–66.
16 Pan, Z., & Liu, M. (2022). The role of adaptive scaffolding system in supporting middle school problem-based
learning activities. Journal of Educational Technology Systems, 51(2), 117–145.
17 Park, J., Lee, J., & Kim, D. (2020). The effects of indexing prompts on problem-solving in case library learning.
Problems of Education in the 21st Century, 78(3), 394–409.
18 Sandra, R. P., Hwang, W. Y., Zafirah, A., Hariyanti, U., Engkizar, E., Hadi, A., & Fauzan, A. (2024). Crafting compelling
argumentative writing for undergraduates: Exploring the nexus of digital annotations, conversational agents,
and collaborative concept maps. Journal of Educational Computing Research, 62(5), 1107–1137.
19 Shin, S., Brush, T. A., & Glazewski, K. D. (2017). Designing and implementing web-based scaffolding tools for
technology-enhanced socioscientific inquiry. Journal of Educational Technology & Society, 20(1), 1–12.
20 Shin, S., & Song, H. D. (2016). Finding the optimal scaffoldings for learners’ epistemological beliefs during ill-
structured problem solving. Interactive Learning Environments, 24(8), 2032–2047.
21 Shin, Y., Kim, D., & Song, D. (2020). Types and timing of scaffolding to promote meaningful peer interaction and
increase learning performance in computer-supported collaborative learning environments. Journal of
Educational Computing Research, 58(3), 640–661.
(Continued)

24 H. JANG ET AL.
(Continued).
22 Sorour, S. E., Ahmed, R. J., & Abd El Aziz, M. I. (2024). A multi-smart agent-based training environment for
enhancing 3D graphics production and design thinking skills among elementary computer teachers. Frontiers
in Education, 9, 1392266
23 Tawfik, A. A., Law, V., Ge, X., Xing, W., & Kim, K. (2018). The effect of sustained vs. faded scaffolding on students’
argumentation in ill-structured problem solving. Computers in Human Behavior, 87, 436–449.
24 Wan, H., Zhang, X., Yang, X., & Li, S. (2024). Which approach is effective: Comparing problematization-oriented
and structuring-oriented scaffolding in instructional videos for programming education. Education and
Information Technologies, 29(14), 17807–17823.
25 Wang, M., Yuan, B., Kirschner, P. A., Kushniruk, A. W., & Peng, J. (2018). Reflective learning with complex problems
in a visualization-based learning environment with expert support. Computers in Human Behavior, 87, 406–415.
26 Wang, T., Zheng, J., Tan, C., & Lajoie, S. P. (2023). Computer‐based scaffoldings influence students’ metacognitive
monitoring and problem‐solving efficiency in an intelligent tutoring system. Journal of Computer Assisted
Learning, 39(5), 1652–1665.
27 WinklerWinkler, R., Söllner, M., & Leimeister, J. M. (2021). Enhancing problem-solving skills with smart personal
assistant technology. Computers & Education, 165, 104148.
28 Yilmaz-Na, E., & Sönmez, E. (2023). Unfolding the potential of computer-assisted argument mapping practices for
promoting self-regulation of learning and problem-solving skills of pre-service teachers and their relationship.
Computers & Education, 193, 104683.
29 Zheng, L., Zhen, Y., Niu, J., & Zhong, L. (2022). An exploratory study on fade-in versus fade-out scaffolding for
novice programmers in online collaborative programming settings. Journal of Computing in Higher Education,
34(2), 489–516.
