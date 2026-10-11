import { useEffect, useState } from 'react';

export type AsyncState<T> =
  | { readonly kind: 'loading' }
  | { readonly kind: 'error'; readonly message: string }
  | { readonly kind: 'ready'; readonly data: T };

// Petit utilitaire partagé par les ViewModels : état d'écran immuable, flux unidirectionnel.
export function useAsyncState<T>(load: () => Promise<T>): AsyncState<T> {
  const [state, setState] = useState<AsyncState<T>>({ kind: 'loading' });

  useEffect(() => {
    let active = true;
    load()
      .then((data) => {
        if (active) setState({ kind: 'ready', data });
      })
      .catch((e: unknown) => {
        if (active) setState({ kind: 'error', message: e instanceof Error ? e.message : 'Erreur inconnue' });
      });
    return () => {
      active = false;
    };
    // `load` doit être stable (fonction de repository).
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return state;
}
