document.addEventListener('DOMContentLoaded', () => {
    const tableContent = document.getElementById('tableContent');
    
    for (let i = 1; i <= 997; i++) {
        const row = document.createElement('div');
        row.className = 'grid grid-cols-5 gap-4 p-4 hover:bg-gray-50';
        
        row.innerHTML = `
            <div>${i}</div>
            <div>Nome${i}</div>
            <div>Sobrenome${i}</div>
            <div>email${i}@exemplo.com</div>
            <div>
                <button class="bg-blue-500 text-white px-2 py-1 rounded mr-2 hover:bg-blue-600">Editar</button>
                <button class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600">Excluir</button>
            </div>
        `;
        
        tableContent.appendChild(row);
    }
});
