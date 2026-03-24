---
title: "Notes"
layout: default
permalink: /notes/
---

<h1>Notes</h1>

{% for post in site.notes %}
  <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
  <p>{{ post.date | date: "%B %d, %Y" }}</p>
{% endfor %}

