import React, { useState } from 'react'
import './App.css'

const API_URL = 'http://localhost:8000'

export default function Login({ onLogin }) {
  const [form, setForm] = useState({ username: '', password: '' })

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value })

  const handleSubmit = e => {
    e.preventDefault()
    fetch(`${API_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    }).then(res => {
      if (res.ok) onLogin()
      else alert('Credenciales incorrectas')
    })
  }

  return (
    <div className="container">
      <h1>Gestor de Socios</h1>
      <form onSubmit={handleSubmit} className="form">
        <input name="username" placeholder="Usuario" value={form.username} onChange={handleChange} required />
        <input name="password" type="password" placeholder="Contraseña" value={form.password} onChange={handleChange} required />
        <button type="submit">Entrar</button>
      </form>
    </div>
  )
}
