import { Component, OnInit } from '@angular/core';
import {Router, ActivatedRoute, Params, RouterLink} from "@angular/router";
import { usuario } from '../modelos/usuario.model';
import { UsuarioService } from '../services/usuario.service';


@Component({
  selector: 'app-editar-perfil',
  templateUrl: './editar-perfil.component.html',
  styleUrls: ['./editar-perfil.component.css'],
  providers: [UsuarioService]
})
export class EditarPerfilComponent implements OnInit {
  
  public usuario: usuario;

  constructor(usuario: usuario){
    this.usuario = usuario;
  }

  ngOnInit(): void {

  }

  actualizarUsuario(){
    

  }

}
