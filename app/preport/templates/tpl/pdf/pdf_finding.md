
## {{finding.title|safe}}

::: {{icon_finding}}
**Schwere:** {{severity_color_finding}}
{% if finding.cvss_base_score != "0" %}
**CVSS Score:** {{finding.cvss_base_score}}
{% endif %}
:::

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

