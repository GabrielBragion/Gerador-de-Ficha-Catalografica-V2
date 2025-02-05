import React from "react";
import styles from "./Ficha.module.css";
import { useGlobalContext } from "../context/GlobalContext";

// Função para converter número para romano

const romanNumerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"];

const Ficha = () => {
	const { globalData } = useGlobalContext();

	if (!globalData) {
		return <div className={styles.ficha}></div>;
	}

	const listaNumerosRomanos = [
		globalData.orientadores_invertidos["orientador"],
		...globalData.alunos_invertidos.slice(1),
		globalData.titulo_subtitulo[0],
	];

	console.log(listaNumerosRomanos);

	return (
		<div className={styles.ficha}>
			<div>
				<p>{globalData.alunos_invertidos[0]}.</p>
				<p className={styles.textIndent}>
					{globalData.titulo_subtitulo[0]}
					{globalData.titulo_subtitulo[1]
						? ":" + globalData.titulo_subtitulo[1]
						: ""} / {globalData.alunos.map((aluno) => aluno).join("; ")}.
				</p>
				<p className={styles.textIndent}>{globalData.ano}.</p>
				<p className={styles.textIndent}>{globalData.total_paginas} f.</p>
			</div>
			<p className={styles.textIndent}>Orientador: {globalData.orientadores["orientador"]}</p>
			{globalData.orientadores["co_orientador"] === "" ||
			globalData.orientadores["co_orientador"] === "Não encontrado" ? (
				""
			) : (
				<p className={styles.textIndent}>
					Coorientador: {globalData.orientadores["co_orientador"]}
				</p>
			)}
			<p className={styles.textIndent}>
				{globalData.tipo_trabalho} - {globalData.universidade_curso[0]},{" "}
				{globalData.universidade_curso[1]}, {globalData.cidade}, {globalData.estado},{" "}
				{globalData.ano}.
			</p>
			<p className={styles.textIndent}>
				{globalData.palavras_chave.map((palavra, idx) => idx + 1 + ". " + palavra).join(". ")}{". "}
				{listaNumerosRomanos.map((item, idx) => romanNumerals[idx] + ". " + item).join(". ")}.
			</p>
		</div>
	);
};

export default Ficha;
