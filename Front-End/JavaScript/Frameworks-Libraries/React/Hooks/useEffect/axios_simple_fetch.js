// Credit ---> https://www.robinwieruch.de/react-hooks-fetch-data

import React, { Fragment, useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState({ hits: [] });
    const [query, setQuery] = useState('redux');
    const [url, setUrl] = useState('https://hn.algolia.com/api/v1/search?query=redux');
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            setIsError(false);
            setIsLoading(true);

            try {
                const result = await axios(url);
                setData(result.data);
            } catch (error) {
                setIsError(true);
            }

            setIsLoading(false);
        };

        fetchData();
    }, [url]);

return (
    <Fragment>
        <input
            type="text"
            value={query}
            onChange={event => setQuery(event.target.value)}
        />
        <button
            type="button"
            onClick={() =>
                setUrl(`http://hn.algolia.com/api/v1/search?query=${query}`)
            }
        >
        Search
        </button>

        {/* Using A Form Instead */}
        <form onSubmit={event => {
            setUrl(`http://hn.algolia.com/api/v1/search?query=${query}`);
    
            event.preventDefault();
        }}>
            <input
                type="text"
                value={query}
                onChange={event => setQuery(event.target.value)}
            />
            <button type="submit">Search</button>
        </form>

        {isError && <div>Something went wrong ...</div>}

        {isLoading ? (
        <div>Loading ...</div>
        ) : (
        <ul>
            {data.hits.map(item => (
            <li key={item.objectID}>
                <a href={item.url}>{item.title}</a>
            </li>
            ))}
        </ul>
        )}
    </Fragment>
);
}
 
export default App;



/*

    CUSTOM DATA FETCHING HOOK

*/ 

import React, { Fragment, useState, useEffect } from 'react';
import axios from 'axios';

const useDataApi = (initialUrl, initialData) => {
    const [data, setData] = useState(initialData);
    const [url, setUrl] = useState(initialUrl);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    
    useEffect(() => {
        const fetchData = async () => {
        setIsError(false);
        setIsLoading(true);
    
        try {
            const result = await axios(url);
    
            setData(result.data);
        } catch (error) {
            setIsError(true);
        }
    
        setIsLoading(false);
        };
    
        fetchData();
    }, [url]);
    
    return [{ data, isLoading, isError }, setUrl];
};

function App() {
    const [query, setQuery] = useState('redux');
    const [{ data, isLoading, isError }, doFetch] = useDataApi(
        'https://hn.algolia.com/api/v1/search?query=redux',
        { hits: [] },
);
 
  return (
    <Fragment>
        <form
            onSubmit={event => {
            doFetch(
                `http://hn.algolia.com/api/v1/search?query=${query}`,
            );
    
            event.preventDefault();
            }}
        >
            <input
            type="text"
            value={query}
            onChange={event => setQuery(event.target.value)}
            />
            <button type="submit">Search</button>
        </form>
    
        {isError && <div>Something went wrong ...</div>}
    
        {isLoading ? (
            <div>Loading ...</div>
        ) : (
            <ul>
            {data.hits.map(item => (
                <li key={item.objectID}>
                <a href={item.url}>{item.title}</a>
                </li>
            ))}
            </ul>
        )}
        </Fragment>
    );
}

export default App;