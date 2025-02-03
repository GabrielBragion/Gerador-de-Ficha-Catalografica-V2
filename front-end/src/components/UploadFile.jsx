import React, { useState, useRef } from "react";
import styles from "./UploadFile.module.css";
import Button from "./Button"; // Importa o botão

const UploadFile = () => {
	const [file, setFile] = useState(null); // Alterei para armazenar um único arquivo
	const [ativo, setAtivo] = useState(false);
	const [loading, setLoading] = useState(false);
	const [dragActive, setDragActive] = useState(false); // Novo estado para drag
	const fileInputRef = useRef(null);

	// Manipula arquivos adicionados
	const handleFile = (file) => {
		if (file) {
			setFile(file); // Armazena o arquivo
			setAtivo(true); // Habilita o botão "Gerar"
		}
	};

	// Simula clique no input escondido
	const handleClick = () => {
		fileInputRef.current.click();
	};

	// Detecta mudança no input
	const handleChange = (e) => {
		if (e.target.files[0]) {
			handleFile(e.target.files[0]); // Apenas o primeiro arquivo
		}
	};

	// Envia o arquivo para o backend
	const handleUpload = async () => {
		if (!file) return; // Verifica se há um arquivo

		const formData = new FormData();
		formData.append("file", file); // Adiciona o arquivo ao formData

		// Marca o início do carregamento
		setLoading(true);

		try {
			const response = await fetch("http://127.0.0.1:5000/upload", {
				method: "POST",
				body: formData,
			});

			// Após o envio, encerra o carregamento
			setLoading(false);

			if (response.ok) {
				const data = await response.json();
				alert("Arquivo enviado com sucesso! 🎉");
				console.log("Resposta do backend:", data);
			} else {
				alert("Erro ao enviar arquivo.");
			}
		} catch (error) {
			// Em caso de erro, encerra o carregamento
			setLoading(false);
			console.error("Erro ao enviar:", error);
			alert("Erro ao enviar arquivo.");
		}
	};

	// Manipula o evento de arrasto sobre a área de drop
	const handleDragOver = (e) => {
		e.preventDefault();
		setDragActive(true); // Ativa o estilo de feedback visual
	};

	// Manipula o evento de saída do arrasto
	const handleDragLeave = () => {
		setDragActive(false); // Desativa o feedback visual
	};

	// Manipula o evento de soltar o arquivo
	const handleDrop = (e) => {
		e.preventDefault();
		setDragActive(false); // Desativa o feedback visual
		if (e.dataTransfer.files.length > 0) {
			handleFile(e.dataTransfer.files[0]); // Apenas o primeiro arquivo
		}
	};

	return (
		<section className={styles.wrapper}>
			{/* Área de drag-and-drop */}
			<div
				className={`${styles.dropzone} ${dragActive ? styles.active : ""}`}
				onClick={handleClick}
				onDragOver={handleDragOver} // Adiciona o evento de arrasto
				onDragLeave={handleDragLeave} // Adiciona o evento de saída
				onDrop={handleDrop} // Adiciona o evento de soltura
			>
				<input
					type="file"
					className={styles.fileInput}
					onChange={handleChange}
					ref={fileInputRef}
				/>
				{file ? (
					<p>
						{/* Exibe o nome do arquivo carregado */}
						<span>{file.name}</span>
					</p>
				) : (
					<p>
						Arraste e solte um arquivo aqui ou{" "}
						<span className={styles.highlight}>clique para selecionar</span>
					</p>
				)}
			</div>

			{/* Botão Gerar com feedback visual */}
			<Button disabled={!ativo || loading} onClick={handleUpload}>
				{loading ? "Enviando..." : "Gerar"}
			</Button>
		</section>
	);
};

export default UploadFile;
