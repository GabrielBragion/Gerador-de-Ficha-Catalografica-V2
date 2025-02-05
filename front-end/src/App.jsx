import Footer from "./components/Footer";
import Header from "./components/Header";
import Main from "./components/Main";

import "normalize.css";
import "./App.css";
import { GlobalProvider } from "./context/GlobalContext";

const App = () => {
	return (
		<>
		<GlobalProvider>
			<Header />
			<Main />
			<Footer />
		</GlobalProvider>
		</>
	);
};

export default App;

