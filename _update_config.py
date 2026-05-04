with open('_config.yml', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('title                    : "Your Name / Site Title"', 'title                    : "Qingzhuo Wang"'),
    ('name                     : &name "Your Name"', 'name                     : &name "Qingzhuo Wang"'),
    ('"Your Name\'s academic portfolio"   # Update this with a general description of your site, this is the default if not overridden by a page', '"Qingzhuo Wang\'s personal academic website"'),
    ('url                      : https://academicpages.github.io # The base hostname & protocol for your site e.g. "https://[your GitHub username].github.io",\n                                                           # or if you already have some other page hosted on Github then use "https://[your GitHub username].github.io/[Your Repo Name]"', 'url                      : https://weiliang822.github.io'),
    ('repository               : "academicpages/academicpages.github.io"', 'repository               : "weiliang822/weiliang822.github.io"'),
    ('  name             : "Your Sidebar Name"', '  name             : "Qingzhuo Wang"'),
    ('  bio              : "Short biography for the left-hand sidebar"', '  bio              : "M.S. student at Tongji University. Interested in LLM post-training, knowledge distillation, and agentic RL."'),
    ('  location         : "Earth"', '  location         : "Shanghai, China"'),
    ('  employer         : "Red Brick University"', '  employer         : "Tongji University"'),
    ('  email            : "none@example.org"', '  email            : "weiliang6272@gmail.com"'),
    ('  googlescholar    : "https://scholar.google.com/citations?user=PS_CX0AAAAAJ"', '  googlescholar    : "https://scholar.google.com.hk/citations?user=hbBbJEIAAAAJ"'),
    ('  orcid            : "https://orcid.org/yourorcidurl"', '  orcid            : #'),
    ('  pubmed           : "https://www.ncbi.nlm.nih.gov/pubmed/?term=john+snow"', '  pubmed           : #'),
    ('  github           : "academicpages"', '  github           : "weiliang822"'),
    ('  bluesky          : "bsky.app" # Replace this with you Bluesky username', '  bluesky          : #'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('_config.yml', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
