import React, { useEffect, useState } from 'react'
import './App.css'
import Login from './Login'

const API_URL = 'http://localhost:8000'

function App() {
  const [logged, setLogged] = useState(false)

  const [socios, setSocios] = useState([])
  const [form, setForm] = useState({
    nombre: '',
    rut: '',
    email: '',
    telefono: '',
    direccion: '',
    fecha_ingreso: ''
  })
  const [pagoForm, setPagoForm] = useState({
    socio_id: '',
    monto: '',
    fecha: '',
    medio: '',
    moneda: 'CLP'
  })
  const [pagos, setPagos] = useState([])

  const [eventoForm, setEventoForm] = useState({
    nombre: '',
    fecha: '',
    descripcion: '',
    pago_requerido: false
  })
  const [eventos, setEventos] = useState([])

  useEffect(() => {
    if (logged) {
      fetch(`${API_URL}/socios/`).then(res => res.json()).then(setSocios)
      fetch(`${API_URL}/pagos/`).then(res => res.json()).then(setPagos)
      fetch(`${API_URL}/eventos/`).then(res => res.json()).then(setEventos)
    }
  }, [logged])

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = e => {
    e.preventDefault()
    fetch(`${API_URL}/socios/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })
      .then(res => res.json())
      .then(newSocio => {
        setSocios([...socios, newSocio])
        setForm({ nombre: '', rut: '', email: '', telefono: '', direccion: '', fecha_ingreso: '' })
      })
  }

  const handleEventoChange = e => {
    const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value
    setEventoForm({ ...eventoForm, [e.target.name]: value })
  }

  const handleEventoSubmit = e => {
    e.preventDefault()
    fetch(`${API_URL}/eventos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...eventoForm, pago_requerido: Boolean(eventoForm.pago_requerido) })
    })
      .then(res => res.json())
      .then(newEvento => {
        setEventos([...eventos, newEvento])
        setEventoForm({ nombre: '', fecha: '', descripcion: '', pago_requerido: false })
      })
  }

  const handlePagoChange = e => {
    setPagoForm({ ...pagoForm, [e.target.name]: e.target.value })
  }

  const handlePagoSubmit = e => {
    e.preventDefault()
    fetch(`${API_URL}/pagos/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(pagoForm)
    })
      .then(res => res.json())
      .then(newPago => {
        setPagos([...pagos, newPago])
        setPagoForm({ socio_id: '', monto: '', fecha: '', medio: '', moneda: 'CLP' })
      })
  }

  if (!logged) {
    return <Login onLogin={() => setLogged(true)} />
  }

  return (
    <div className="App container">
      <h1>Gestor de Socios</h1>

      <h2>Nuevo Socio</h2>
      <form onSubmit={handleSubmit} className="form">
        <input name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} required />
        <input name="rut" placeholder="RUT" value={form.rut} onChange={handleChange} required />
        <input name="email" type="email" placeholder="Email" value={form.email} onChange={handleChange} required />
        <input name="telefono" placeholder="Teléfono" value={form.telefono} onChange={handleChange} />
        <input name="direccion" placeholder="Dirección" value={form.direccion} onChange={handleChange} />
        <input name="fecha_ingreso" type="date" value={form.fecha_ingreso} onChange={handleChange} required />
        <button type="submit">Guardar</button>
      </form>

      <h2>Socios</h2>
      <ul>
        {socios.map(s => (
          <li key={s.id}>{s.nombre} - {s.rut} - {s.email}</li>
        ))}
      </ul>

      <h2>Registrar Pago</h2>
      <form onSubmit={handlePagoSubmit} className="form">
        <input name="socio_id" placeholder="ID Socio" value={pagoForm.socio_id} onChange={handlePagoChange} required />
        <input name="monto" placeholder="Monto" value={pagoForm.monto} onChange={handlePagoChange} required />
        <input name="fecha" type="datetime-local" value={pagoForm.fecha} onChange={handlePagoChange} required />
        <input name="medio" placeholder="Medio" value={pagoForm.medio} onChange={handlePagoChange} required />
        <input name="moneda" placeholder="Moneda" value={pagoForm.moneda} onChange={handlePagoChange} />
        <button type="submit">Guardar</button>
      </form>

      <h2>Pagos</h2>
      <ul>
        {pagos.map(p => (
          <li key={p.id}>Socio {p.socio_id} - {p.monto} {p.moneda} - {new Date(p.fecha).toLocaleString()}</li>
        ))}
      </ul>
      <h2>Nuevo Evento</h2>
      <form onSubmit={handleEventoSubmit} className="form">
        <input name="nombre" placeholder="Nombre" value={eventoForm.nombre} onChange={handleEventoChange} required />
        <input name="fecha" type="datetime-local" value={eventoForm.fecha} onChange={handleEventoChange} required />
        <input name="descripcion" placeholder="Descripción" value={eventoForm.descripcion} onChange={handleEventoChange} />
        <label>
          <input type="checkbox" name="pago_requerido" checked={eventoForm.pago_requerido} onChange={handleEventoChange} /> Requiere pago
        </label>
        <button type="submit">Guardar</button>
      </form>

      <h2>Eventos</h2>
      <ul>
        {eventos.map(e => (
          <li key={e.id}>{e.nombre} - {new Date(e.fecha).toLocaleString()}</li>
        ))}
      </ul>
    </div>
  )
}

export default App
