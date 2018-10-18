data Quant a b = Finance | Desk a | Floor b deriving (Show, Eq)

instance Functor (Quant a) where
    fmap _ Finance   = Finance
    fmap f (Desk a)  = Desk a
    fmap f (Floor b) = Floor (f b)
