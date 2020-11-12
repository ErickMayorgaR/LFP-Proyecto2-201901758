import { Injectable } from '@angular/core';
import { usuario } from '../modelos/usuario.model';
import {Global} from '../services/global.service';
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Observable } from 'rxjs';
import { JsonPipe } from '@angular/common';
@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  public url: string;
  
  constructor(public _http: HttpClient) {this.url = Global.url; }

  getUsuarios(){
    return this._http.get(this.url+'usuarios');
  }

  getUsuario(usuario: usuario): Observable<any>{
    let params = JSON.stringify(usuario)
    let header = new HttpHeaders().set('Content-Type','application/json')
    return this._http.get(this.url+'usuario/'+usuario._id, {headers: header});
  }

  crearUsuario(usuario:usuario): Observable<any>{
    let params = JSON.stringify(usuario)
    let header = new HttpHeaders().set('Content-Type', 'application/json')
    return this._http.post(this.url+'crearUsuario',params,{headers:header})
  }

  actualizarUsuario(usuario:usuario):Observable<any>{
      let params = JSON.stringify(usuario);
      let headers = new HttpHeaders().set('Content-Type','application/json');
  
      return this._http.put(this.url+'actualizarUsuario/'+usuario._id, params, {headers: headers});
  }
  deleteUser(usuario: usuario): Observable<any>{
    let headers = new HttpHeaders().set('Content-Type','application/json');
    return this._http.delete(this.url+'eliminarUsuario/'+usuario._id, {headers: headers});
  }

  login(user): Observable<any>{
    let params = JSON.stringify(user);
    let headers = new HttpHeaders().set('Content-Type', 'application/json');
    return this._http.post(this.url+'login', params, {headers: headers});
  }
}

