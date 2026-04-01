import re

# BaseJpaConfig.md
with open(r'D:\Sarlaft 4.0\docs\MicroservicioBackweb\BaseJpaConfig.md', encoding='utf-8') as f:
    c = f.read()
c = c.replace('```\npackage com.sura.backweb.config', '```java\npackage com.sura.backweb.config')
c = c.replace('\t', '    ')
with open(r'D:\Sarlaft 4.0\docs\MicroservicioBackweb\BaseJpaConfig.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(c)
print('BaseJpaConfig: tabs left:', c.count('\t'))

# EstructuraProyecto.md
with open(r'D:\Sarlaft 4.0\docs\MicroservicioBackweb\EstructuraProyecto.md', encoding='utf-8') as f:
    c = f.read()

# Fix broken list items: -\n**item** -> - **item**
c = re.sub(r'\n-\n\*\*model\*\*:', '\n- **model**:', c)
c = re.sub(r'\n-\n\*\*use-case\*\*:', '\n- **use-case**:', c)
c = re.sub(r'\n-\n\*\*driven-adapters-async-messages-senders: \*\*', '\n- **driven-adapters-async-messages-senders:** ', c)
c = re.sub(r'\n-\n\*\*driven-adapters-jpa-repository: \*\*', '\n- **driven-adapters-jpa-repository:** ', c)
c = re.sub(r'\n-\n\*\*entry-points-reactive-web: \*\*', '\n- **entry-points-reactive-web:** ', c)

# Add language to code fences
c = c.replace('Properties\n\n```\nspring:', 'Properties\n\n```yaml\nspring:')
c = c.replace('Configuration\n\n```\n...', 'Configuration\n\n```java\n...')
c = c.replace('\n}\n}\n```', '\n}\n}\n```\n')

with open(r'D:\Sarlaft 4.0\docs\MicroservicioBackweb\EstructuraProyecto.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(c)
print('EstructuraProyecto done')
