import React, { useEffect, useState } from 'react'
import './App.css'

const API_URL = 'http://localhost:8000'

function App() {
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

  useEffect(() => {
    fetch(`${API_URL}/socios/`).then(res => res.json()).then(setSocios)
    fetch(`${API_URL}/pagos/`).then(res => res.json()).then(setPagos)
  }, [])

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

  return (
    <div className="App" style={{ padding: '1rem' }}>
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
    </div>
  )
}

export default App
