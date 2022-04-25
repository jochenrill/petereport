
## {{finding.title|safe}}

::: {{icon_finding}}
**Schwere:** {{severity_color_finding}}

**CVSS Score:** {{finding.cvss_base_score}}
:::

**CWE**

{{finding.cwe.cwe_id}} - {{finding.cwe.cwe_name|safe}}

**Beschreibung**

{{finding.description|safe}}

{% if finding.location %}
**Ort**

{{finding.location|safe}}

{% endif %}

**Auswirkung**

{{finding.impact|safe}}

**Empfehlung**

{{finding.recommendation|safe}}

{% if finding.references %}
**Referenzen**

{{finding.references|safe}}

{% endif %}

{% if template_appendix_in_finding %}
{{template_appendix_in_finding|safe}}
{% endif %}

{% if template_attacktree_in_finding %}
{{template_attacktree_in_finding|safe}}
{% endif %}

