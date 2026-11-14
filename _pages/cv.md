---
title: "CV"
permalink: /cv/
---
{% comment %}
  To update the CV: upload the new PDF to the /files/ folder under the
  file name set in _config.yml (cv_file), replacing the old one.
  The download link appears automatically once the file exists.
{% endcomment %}
{% include base_path %}
{% assign cv_path = "/files/" | append: site.cv_file %}
{% assign cv = site.static_files | where: "path", cv_path | first %}
{% if cv %}
<p><a class="cv-download" href="{{ base_path }}{{ cv_path }}"><i class="fas fa-file-pdf" aria-hidden="true"></i> Download CV (PDF)</a></p>
{% else %}
<p class="muted">A PDF copy of my CV will be available here shortly.</p>
{% endif %}
