{% extends "base.html" %}

{% block content %}

<h1>Add Mood</h1>

<div>
  <form action="{% url 'add_albums' %}" method="POST">
      {% csrf_token %}
      {{ form.as_p }}
      <div>
       <button type="submit">Add Album</button>
      </div>
  </form>
   <p><a href="{% url 'list_moods' %}">Mood Chart </a></p>
  </div>

{% endblock %}